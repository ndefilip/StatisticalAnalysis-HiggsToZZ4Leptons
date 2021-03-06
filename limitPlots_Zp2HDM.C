// -----------------------------------------------------------------------------
//  File:        limitPlots_Zp2HDM.C
//  Usage:       root -b -q -l "limitPlots_Zp2HDM.C(\"4mu\")"
//  Description: Parse the simple limits file limits_*_13tev_out.txt and plot.
//  Created:     5-July-2016 Dustin Burns
// -----------------------------------------------------------------------------
#include <sstream>


void limitPlots_Zp2HDM(std::string channel){

// Parse input file, filling arrays for plots
stringstream ss;
ss << "limits_Zp2HDM_" << channel << "_MA0300_out.txt" ;
std::ifstream file( ss.str().c_str() );
std::string str;
char delim = ' ';
std::string item;
std::vector<std::string> elems;
static const Int_t n = 8;
//Double_t _mzp[n] = {600, 800, 1000, 1200, 1400};
//Double_t _mzp[n] = {600, 800, 1000, 1200, 1400, 1700};
 Double_t _mzp[n] = {600, 800, 1000, 1200, 1400, 1700, 2000, 2500};
Double_t _2siglow[n];
Double_t _1siglow[n];
Double_t _middle[n];
Double_t _1sighigh[n];
Double_t _2sighigh[n];
Double_t _observed[n];
int lin = 0;
while (std::getline(file, str)){
  lin++;
  std::stringstream ss(str);
  Int_t i = -1;
  while (std::getline(ss, item, delim)){
    i++;
    elems.push_back(item);
    if (lin == 1 && i < n) {
      _2siglow[i] = atof(item.c_str());
    }
    if (lin == 2 && i < n) {
      _1siglow[i] = atof(item.c_str());
    }
    if (lin == 3 && i < n) {
      _middle[i] = atof(item.c_str());
    }
    if (lin == 4 && i < n) {
      _1sighigh[i] = atof(item.c_str());
    }
    if (lin == 5 && i < n) {
      _2sighigh[i] = atof(item.c_str());
    }
    if (lin == 6 && i < n) {
      _observed[i] = atof(item.c_str());
    }
  }
}


// Scale signal strength limits by signal production cross sections
//Double_t _xsec[n] = {0.000124120665, 0.000076214925, 0.000039481335, 0.0000207112995, 0.000011311596};
//Double_t _xsec[n] = {0.000124120665, 0.000076214925, 0.000039481335, 0.0000207112995, 0.000011311596, 0.000004882257};
//Double_t _xsec[n] = {0.000124120665*1E3, 0.000076214925*1E3, 0.000039481335*1E3, 0.0000207112995*1E3, 0.000011311596*1E3, 0.000004882257*1E3, 0.00000225960165*1E3, 0.0000006988221*1E3};
Double_t BR = 2.745E-04;
Double_t PBtoFB = 1E3;
//Double_t _xsecth[n] = {0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};
//Double_t _xsec[n] = {0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};
 Double_t _xsecth[n] = {0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};
 Double_t _xsec[n] = {0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};
//Double_t _xsec[n] = {0.45217*BR*PBtoFB, 0.27765*BR*PBtoFB, 0.14383*BR*PBtoFB, 0.075451*BR*PBtoFB, 0.041208*BR*PBtoFB*1000, 0.017786*BR*PBtoFB*1000, 0.0082317*BR*PBtoFB*1000, 0.0025458*BR*PBtoFB*1000};
//Double_t _xsec[n] = {BR*PBtoFB, BR*PBtoFB, BR*PBtoFB, BR*PBtoFB, BR*PBtoFB, BR*PBtoFB, BR*PBtoFB, BR*PBtoFB};
//Double_t _xsec[n] = {1, 1, 1, 1, 1, 1, 1, 1};
for(int i=0;i<n;i++){
  _2siglow[i]  *= _xsec[i];
  _1siglow[i]  *= _xsec[i];
  _middle[i]   *= _xsec[i];
  _1sighigh[i] *= _xsec[i];
  _2sighigh[i] *= _xsec[i];
  _observed[i] *= _xsec[i];
}
//cout << "2HDM " << _middle[0] << endl;
//cout << _middle[0] << " " << _middle[1] << " " << _middle[2] << " " << _middle[3] << " " << _middle[4] << " " << _middle[5] << " " << _middle[6] << " " << _middle[7] << endl;


// Fill graphs
TGraph *g2siglow  = new TGraph(n, _mzp, _2siglow);
TGraph *g1siglow  = new TGraph(n, _mzp, _1siglow);
TGraph *gmiddle   = new TGraph(n, _mzp, _middle);
TGraph *g1sighigh = new TGraph(n, _mzp, _1sighigh);
TGraph *g2sighigh = new TGraph(n, _mzp, _2sighigh);
TGraph *gobserved = new TGraph(n, _mzp, _observed);
TGraph *gxsec     = new TGraph(n, _mzp, _xsecth);
TGraph *grshade1   = new TGraph(2*n);
TGraph *grshade2   = new TGraph(2*n);
for(int i=0;i<n;i++){
  grshade1->SetPoint(i, _mzp[i], _1sighigh[i]);
  grshade1->SetPoint(n+i, _mzp[n-i-1], _1siglow[n-i-1]);
}
for(int i=0;i<n;i++){
  grshade2->SetPoint(i, _mzp[i], _2sighigh[i]);
  grshade2->SetPoint(n+i, _mzp[n-i-1], _2siglow[n-i-1]);
}

// Write to file
TFile * fout   = new TFile("ZZ_plots_theoryxsec.root", "recreate");
g2siglow->Write("g2siglow");
g1siglow->Write("g1siglow");
gmiddle->Write("gmiddle");
g1sighigh->Write("g1sighigh");
g2sighigh->Write("g2sighigh");

// Plot formatting
gStyle->SetOptStat(0);
TCanvas *c = new TCanvas("c");
c->cd();
//c->SetLogx();
c->SetLogy();
c->SetTicks(1,1);
c->SetGrid();
//TH2F * hframe = new TH2F("hframe", "", 10, 600, 2500, 10, 1E-2, 1E4);
TH2F * hframe = new TH2F("hframe", "", 10, 600, 1700, 10, 5E-3, 20.);
//hframe->GetXaxis()->SetTitle("m_{Z'} [GeV]");
//hframe->GetXaxis()->SetTitleOffset(1.0);
//hframe->GetXaxis()->SetTitleSize(0.04);
//if (strncmp(channel.c_str(), "4mu", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi #mu#mu#mu#mu) [fb]");
//if (strncmp(channel.c_str(), "4e", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi eeee) [fb]");
//if (strncmp(channel.c_str(), "2e2mu", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi ee#mu#mu) [fb]");
//if (strncmp(channel.c_str(), "4l", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi llll) [fb]");
//hframe->GetYaxis()->SetTitle("#sigma_{95%CL} / #sigma_{theory}");
//hframe->GetYaxis()->SetTitleOffset(1.0);
//hframe->GetYaxis()->SetTitleSize(0.04);
//hframe->Draw();

hframe->SetYTitle("95% C.L. #sigma(pp #rightarrow Z'H #rightarrow #chi #chi llll) (fb)");
hframe->GetYaxis()->SetLabelSize(0.035);
hframe->GetYaxis()->SetTitleSize(0.032);
hframe->GetYaxis()->SetLabelOffset(0.007);
hframe->GetYaxis()->SetTitleOffset(1.35);
hframe->GetYaxis()->SetTickLength(0.02);
hframe->GetXaxis()->SetTitle("m_{Z'} (GeV)");
hframe->GetXaxis()->SetLabelSize(0.035);
hframe->GetXaxis()->SetTitleSize(0.032);
hframe->GetXaxis()->SetLabelOffset(0.007);
hframe->GetXaxis()->SetTitleOffset(1.35);
hframe->GetXaxis()->SetTickLength(0.02);
hframe->Draw("Same");

grshade2->SetFillColor(5);
grshade2->Draw("f");
grshade1->SetFillColor(3);
grshade1->Draw("f");
gmiddle->SetLineWidth(2);
gmiddle->SetLineStyle(2);
gmiddle->Draw("l");
gobserved->SetLineWidth(2);
gobserved->Draw("l");
gxsec->SetLineWidth(2);
gxsec->SetLineColor(kBlue);
gxsec->SetLineStyle(2);
gxsec->Draw("l");


// Legend formatting
TLegend *leg = new TLegend(0.7,0.65,0.85,0.85);
leg->SetFillStyle(0);
leg->SetBorderSize(0);
leg->AddEntry(gxsec, "Z'2HDM x BR", "L");
leg->AddEntry(gmiddle, "Expected limit", "L");
leg->AddEntry(grshade1, "#pm 1 #sigma", "F");
leg->AddEntry(grshade2, "#pm 2 #sigma", "F");
leg->AddEntry(gobserved, "Observed limit", "L");
leg->SetTextSize(0.032);
leg->Draw();


// Text formatting
TPaveText *ll = new TPaveText(0.09, 0.9, 0.92, 0.94, "NDC");
ll->SetTextSize(0.032);
ll->SetTextFont(42);
ll->SetFillColor(0);
ll->SetBorderSize(0);
ll->SetMargin(0.01);
ll->SetTextAlign(12);
TString text = "#font[22]{CMS} #font[12]{Preliminary}";
ll->AddText(0.01,0.5,text);
text = "35.9 fb^{-1} (13 TeV)";
ll->AddText(0.79, 0.5, text);
ll->Draw();


// Save plot
char savepdf[50],saveeps[50],savepng[50];
sprintf(savepdf, "plots/sigma_limits_%s_Zp2HDM.pdf", channel.c_str());
c->SaveAs(savepdf);
sprintf(saveeps, "plots/sigma_limits_%s_Zp2HDM.eps", channel.c_str());
c->SaveAs(saveeps);
sprintf(savepng, "plots/sigma_limits_%s_Zp2HDM.png", channel.c_str());
c->SaveAs(savepng);

/*
//2D Plot
//3.0234 2.4141 2.5234 2.7109 2.9141 3.2656 3.6719 4.4062
//4.1719 2.3984 2.4141 2.6328 2.8203 3.1719 3.6406 4.2969
//0.0000 2.7422 2.3828 2.5547 2.7578 3.1406 3.5781 4.3125
//0.0000 3.4219 2.3672 2.4141 2.7109 3.0547 3.4219 4.1719
//0.0000 0.0000 2.5703 2.3828 2.5703 0.0000 3.3906 4.0938
//0.0000 0.0000 2.9453 0.0000 2.4766 0.0000 0.0000 3.9062

//Double_t _sig[48] = {3.0234, 2.4141, 2.5234, 2.7109, 2.9141, 3.2656, 3.6719, 4.4062, 4.1719, 2.3984, 2.4141, 2.6328, 2.8203, 3.1719, 3.6406, 4.2969, 0.0000, 2.7422, 2.3828, 2.5547, 2.7578, 3.1406, 3.5781, 4.3125, 0.0000, 3.4219, 2.3672, 2.4141, 2.7109, 3.0547, 3.4219, 4.1719, 0.0000, 0.0000, 2.5703, 2.3828, 2.5703, 0.0000, 3.3906, 4.0938, 0.0000, 0.0000, 2.9453, 0.0000, 2.4766, 0.0000, 0.0000, 3.9062};
Double_t _sig[38] = {3.0234, 2.4141, 2.5234, 2.7109, 2.9141, 3.2656, 3.6719, 4.4062, 4.1719, 2.3984, 2.4141, 2.6328, 2.8203, 3.1719, 3.6406, 4.2969, 2.7422, 2.3828, 2.5547, 2.7578, 3.1406, 3.5781, 4.3125, 3.4219, 2.3672, 2.4141, 2.7109, 3.0547, 3.4219, 4.1719, 2.5703, 2.3828, 2.5703, 3.3906, 4.0938, 2.9453, 2.4766, 3.9062};
//Double_t _xsec_th[n] = {0.45217, 0.27765, 0.14383, 0.075451, 0.041208, 0.017786, 0.0082317, 0.0025458,0.45217, 0.27765, 0.14383, 0.075451, 0.041208, 0.017786, 0.0082317, 0.0025458, 0.45217, 0.27765, 0.14383, 0.075451, 0.041208, 0.017786, 0.0082317, 0.0025458, };
for(int i=0;i<38;i++){
  _sig[i]  *= BR*PBtoFB;
}
Double_t _mzp2d[38] = {600, 800, 1000, 1200, 1400, 1700, 2000, 2500, 600, 800, 1000, 1200, 1400, 1700, 2000, 2500, 800, 1000, 1200, 1400, 1700, 2000, 2500, 800, 1000, 1200, 1400, 1700, 2000, 2500, 1000, 1200, 1400, 2000, 2500, 1000, 1400, 2500};
Double_t _ma0[48] = {300, 300, 300, 300, 300, 300, 300, 300, 400, 400, 400, 400, 400, 400, 400, 400, 500, 500, 500, 500, 500, 500, 500, 600, 600, 600, 600, 600, 600, 600, 700, 700, 700, 700, 700, 800, 800, 800};

TCanvas *c1 = new TCanvas("c", "", 800, 600);
c1->cd();
c1->SetRightMargin(0.15);
//c1->SetLogz();
   TPad *pad1 = new TPad("pad1","",0,0,1,1);
   TPad *pad2 = new TPad("pad2","",0,0,1,1);
   pad1->SetRightMargin(0.15);
   pad2->SetRightMargin(0.15);
   pad2->SetFillColor(0);
   pad2->SetFillStyle(4000);
   pad2->SetFrameFillStyle(0);

   pad1->Draw();
   pad1->cd();
//TH2F * hframe1 = new TH2F("hframe1", "", 8, 600, 2500, 6, 300, 800);
//TH2F * hframe = new TH2F("hframe", "", 10, 600, 2500, 10, 5E-5, 8E3);
//hframe1->GetXaxis()->SetTitle("m_{Z'} [GeV]");
//hframe1->GetXaxis()->SetTitleOffset(1.0);
//hframe1->GetXaxis()->SetTitleSize(0.04);
TGraph2D *g2d = new TGraph2D(38, _mzp2d, _ma0, _sig);
g2d->SetNpx(8);
g2d->SetNpy(6);
g2d->SetTitle("");
g2d->Draw("COLZ");
gPad->Update();
g2d->GetXaxis()->SetTitle("m_{Z'} [GeV]");
g2d->GetXaxis()->SetTitleOffset(1.0);
g2d->GetXaxis()->SetTitleSize(0.04);
g2d->GetYaxis()->SetTitle("m_{A0} [GeV]");
g2d->GetYaxis()->SetTitleOffset(1.0);
g2d->GetYaxis()->SetTitleSize(0.04);

TH1F *dummy = new TH1F("dummy", "", 100, 0, 100);
dummy->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi llll) [fb]");
dummy->GetYaxis()->SetTitleSize(0.04);
dummy->GetYaxis()->SetTitleOffset(1.8);
dummy->GetXaxis()->SetLabelOffset(100.0);
dummy->Draw("Y+");
   pad2->Draw();
   pad2->cd();
   dummy->Draw("Y+");
g2d->Draw("TEXTCOLZ");
gPad->Update();
//hframe1->Draw("SAME");
ll->Draw();
c1->SaveAs("plots/sigma_limits_2D_Zp2HDM.png");

*/


}
