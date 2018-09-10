// -----------------------------------------------------------------------------
//  File:        limitPlots_Zp2HDM_Tree.C
//  Usage:       root -b -q -l "limitPlots_Zp2HDM_Tree.C(\"4mu\")"
//  Description: Parse the simple limits file limits_*_13tev_out.txt and plot.
//  Created:     5-July-2016 Dustin Burns
// -----------------------------------------------------------------------------
#include "TFile.h"

void limitPlots_Zp2HDM_Tree(std::string channel){


static const Int_t n = 10;
Int_t _mzpint[n] = {450, 500, 600, 800, 1000, 1200, 1400, 1700, 2000, 2500};
Double_t _mzp[n] = {450, 500, 600, 800, 1000, 1200, 1400, 1700, 2000, 2500};

char histofile[500];
TFile *f=NULL;
TTree *t=NULL;

Double_t _2siglow[n];
Double_t _1siglow[n];
Double_t _middle[n];
Double_t _1sighigh[n];
Double_t _2sighigh[n];
Double_t _observed[n];

TH1F *obslimit = NULL; 
TH1F *explimit = NULL;
TH1F *onesigmaup = NULL;
TH1F *onesigmadown = NULL;
TH1F *twosigmaup = NULL;
TH1F *twosigmadown = NULL;

for (int i=0; i<n; i++){
  sprintf(histofile,"datacards_%s/higgsCombine_hhxx_Spring16_card_%s_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-%d_MA0-300_13TeV-madgraph-pythia8.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);
  //sprintf(histofile,"datacards_%s/higgsCombine_%s_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-%d_MA0-300_13TeV-madgraph-pythia8.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);
  if (i<=1) sprintf(histofile,"datacards_%s/higgsCombine_hhxx_Spring16_card_%s_ZprimeToA0hToA0chichihZZTo4l_2HDM_13TeV-madgraph_Target_MZp-%d_MA0-300_Ref_600_300_reweighted.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);
  //if (i<=1) sprintf(histofile,"datacards_%s/higgsCombine_%s_ZprimeToA0hToA0chichihZZTo4l_2HDM_13TeV-madgraph_Target_MZp-%d_MA0-300_Ref_600_300_reweighted.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);

  cout << "Opening " << histofile << endl;
  f=TFile::Open(histofile); 
  t=(TTree*)f->Get("limit");
  obslimit = new TH1F("obslimit", "obslimit", 1, -100000., 100000.);
  // t->Scan("limit","quantileExpected==-1"); // Observed
  t->Project("obslimit","limit","quantileExpected==-1"); 
  // cout << "Obs limit= " << obslimit->GetMean() << endl;
  _observed[i]=obslimit->GetMean();

  // t->Scan("limit","quantileExpected==0.5"); // Median
  explimit = new TH1F("explimit", "explimit", 1, -100000., 100000.); 
  t->Project("explimit","limit","quantileExpected==0.5"); // Median
  _middle[i]=explimit->GetMean();

  //t->Scan("limit","abs(quantileExpected-0.1599999)<0.01"); // +1 sigma
  onesigmadown = new TH1F("onesigmadown", "onesigmadown", 1, -100000., 100000.);
  t->Project("onesigmadown","limit","abs(quantileExpected-0.1599999)<0.01"); // -1 sigma
  _1siglow[i]=onesigmadown->GetMean();

  //t->Scan("limit","abs(quantileExpected-0.8399999)<0.01"); // -1 sigma
  onesigmaup = new TH1F("onesigmaup", "onesigmaup", 1, -100000., 100000.);
  t->Project("onesigmaup","limit","abs(quantileExpected-0.8399999)<0.01"); // +1 sigma
  _1sighigh[i]=onesigmaup->GetMean();   
 
  //t->Scan("limit","abs(quantileExpected-0.0250000)<0.01"); // +2 sigma
  twosigmadown = new TH1F("twosigmadown", "twosigmadown", 1, -100000., 100000.);
  t->Project("twosigmadown","limit","abs(quantileExpected-0.0250000)<0.01"); // -2 sigma
  _2siglow[i]=twosigmadown->GetMean();

  //t->Scan("limit","abs(quantileExpected-0.9750000)<0.01"); // -2 sigma
  twosigmaup = new TH1F("twosigmaup", "twosigmaup", 1, -100000., 100000.);
  t->Project("twosigmaup","limit","abs(quantileExpected-0.9750000)<0.01"); // +2 sigma
  _2sighigh[i]=twosigmaup->GetMean(); 

  f->Close();

}


// Scale signal strength limits by signal production cross sections
Double_t BR;
 
 TString tchannel=channel.c_str();
 
// if (tchannel.Contains("4l")){
   BR=2.745E-04;
// }
// else if (tchannel.Contains("4e") || tchannel.Contains("4mu")){
//   BR=3.254E-05;
// }
// else if (tchannel.Contains("2e2mu")){
//   BR=5.897E-05;
// }
 
 cout << "BR is= " << BR << endl;

Double_t PBtoFB = 1E3;
Double_t _xsecth[n] = {0.1447*BR*PBtoFB,0.3416*BR*PBtoFB,0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};
Double_t _xsec[n] = {0.1447*BR*PBtoFB,0.3416*BR*PBtoFB,0.46204*BR*PBtoFB, 0.28501*BR*PBtoFB, 0.14805*BR*PBtoFB, 0.078074*BR*PBtoFB, 0.042734*BR*PBtoFB, 0.018533*BR*PBtoFB, 0.0086088*BR*PBtoFB, 0.0026796*BR*PBtoFB};

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



// Plot formatting
gStyle->SetOptStat(0);
TCanvas *c = new TCanvas("c");
c->cd();
c->SetLogx();
c->SetLogy();
c->SetTicks(1,1);
c->SetGrid();
TH2F * hframe = new TH2F("hframe", "", 10, 450, 2500, 10, 1E-3, 50);
//TH2F * hframe = new TH2F("hframe", "", 10, 450, 2500, 10, 1E-3, 20);
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

gPad->RedrawAxis();

// Legend formatting
//TLegend *leg = new TLegend(0.7,0.67,0.85,0.87);
//TLegend *leg = new TLegend(0.7,0.25,0.85,0.45);
TLegend *leg = new TLegend(0.15,0.15,0.35,0.35);
//leg->SetFillStyle(0);
leg->SetBorderSize(0);
leg->SetTextAlign(12);
leg->AddEntry(gxsec, "Z'_{2HDM} x BR", "L");
leg->AddEntry(gmiddle, "Expected limit", "L");
leg->AddEntry(grshade1, "#pm 1 #sigma", "F");
leg->AddEntry(grshade2, "#pm 2 #sigma", "F");
leg->AddEntry(gobserved, "Observed limit", "L");
leg->SetTextSize(0.032);
leg->SetFillColor(kWhite);
leg->Draw("same");

TPaveText *leg0 = new TPaveText(0.3, 0.73, 0.65, 0.87, "NDC");
leg0->SetTextSize(0.032);
leg0->SetTextFont(42);
leg0->SetFillColor(0);
leg0->SetBorderSize(0);
leg0->SetMargin(0.01);
leg0->SetTextAlign(12);
TString te1 = "Z'-2HDM, mono-H, H #rightarrow ZZ #rightarrow 4l";
leg0->AddText(0.1,0.8,te1);
TString te2 = "g_{Z} = 0.8, g_{#chi} = 1, tan#beta = 1";
leg0->AddText(0.1,0.45,te2);
TString te3 = "m_{A^{0}} = 300 GeV, m_{#chi}= 100 GeV";
leg0->AddText(0.1,0.1,te3);
leg0->Draw("same");


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
ll->Draw("same");


// Save plot
 char savepdf[50], saveeps[50], savepng[50], saveroot[50];
sprintf(savepdf, "plots/sigma_limits_%s_Zp2HDM.pdf", channel.c_str());
c->SaveAs(savepdf);
sprintf(saveeps, "plots/sigma_limits_%s_Zp2HDM.eps", channel.c_str());
c->SaveAs(saveeps);
sprintf(savepng, "plots/sigma_limits_%s_Zp2HDM.png", channel.c_str());
c->SaveAs(savepng);

// Write to file
char foutroot[50];
sprintf(foutroot,"plots/sigma_limits_%s_Zp2HDM.root", channel.c_str());
TFile * fout   = new TFile(foutroot, "recreate");
fout->cd();
g2siglow->Write("g2siglow");
g1siglow->Write("g1siglow");
g1sighigh->Write("g1sighigh");
g2sighigh->Write("g2sighigh");
grshade1->Write("grshade1");
grshade2->Write("grshade2");
gmiddle->Write("gmiddle");
gobserved->Write("gobserved");
gxsec->Write("gxsec");
fout->Write();
fout->Close();

}
