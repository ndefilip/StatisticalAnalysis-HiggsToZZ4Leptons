// -----------------------------------------------------------------------------
//  File:        limitPlots_Zp2HDM_Tree.C
//  Usage:       root -b -q -l "limitPlots_Zp2HDM_Tree.C(\"4mu\")"
//  Description: Parse the simple limits file limits_*_13tev_out.txt and plot.
//  Created:     Nicola De Filippis
// -----------------------------------------------------------------------------


void limitPlots_ZpBaryonic_Tree(std::string channel){

static const Int_t n = 9;

Int_t _mzpint[n] = {10, 20, 50, 100, 200, 300, 500, 1000, 2000};
Double_t _mzp[n] = {10, 20, 50, 100, 200, 300, 500, 1000, 2000};

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

  sprintf(histofile,"datacards_%s/higgsCombine_hhxx_Spring16_card_%s_MonoHZZ4l_ZpBaryonic_MZp-%d_MChi-1_13TeV-madgraph.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);
  //sprintf(histofile,"datacards_%s/higgsCombine_%s_MonoHZZ4l_ZpBaryonic_MZp-%d_MChi-1_13TeV-madgraph.AsymptoticLimits.mH125.root",channel.c_str(),channel.c_str(),_mzpint[i]);
   
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

 Double_t BR;
 
 TString tchannel=channel.c_str();
 
 if (tchannel.Contains("4l")){
   BR=2.745E-04;
 }
 else if (tchannel.Contains("4e") || tchannel.Contains("4mu")){
   BR=3.254E-05;
 }
 else if (tchannel.Contains("2e2mu")){
   BR=5.897E-05;
 }
 
 cout << "BR is= " << BR << endl;

Double_t PBtoFB = 1E3;
Double_t _xsec[n] = {2.59475200139*BR*PBtoFB, 2.72240963862*BR*PBtoFB, 3.2754*BR*PBtoFB, 3.1925*BR*PBtoFB, 2.5604*BR*PBtoFB, 2.2678*BR*PBtoFB, 1.0969*BR*PBtoFB, 0.20100*BR*PBtoFB, 0.014010*BR*PBtoFB};
Double_t _xsecth[n] = {2.59475200139*BR*PBtoFB, 2.72240963862*BR*PBtoFB, 3.2754*BR*PBtoFB, 3.1925*BR*PBtoFB, 2.5604*BR*PBtoFB, 2.2678*BR*PBtoFB, 1.0969*BR*PBtoFB, 0.20100*BR*PBtoFB, 0.014010*BR*PBtoFB};

for(int i=0;i<n;i++){
  _2siglow[i]  *= _xsec[i];
  _1siglow[i]  *= _xsec[i];
  _middle[i]   *= _xsec[i];
  _1sighigh[i] *= _xsec[i];
  _2sighigh[i] *= _xsec[i];
  _observed[i] *= _xsec[i];
}

//cout << "Baryonic " << endl;
// cout << "Expected LIMS: " << _middle[0] << " " << _middle[1] << " " << _middle[2] << " " << _middle[3] << " " << _middle[4] << " " << _middle[5] << " " << _middle[6] << " " << _middle[7] << " " << _middle[8] << endl;
//cout << "Observed LIMS: " << _observed[0] << " " << _observed[1] << " " << _observed[2] << " " << _observed[3] << " " << _observed[4] << " " << _observed[5] << " " << _observed[6] << " " << _observed[7] << " " << _observed[8] << endl;

 cout << "Baryonic " << endl;
 // cout << "Expected LIMS mu: " << _middle[0] << " " << _middle[1] << " " << _middle[2] << " " << _middle[3] << " " << _middle[4] << " " << _middle[5] << " " << _middle[6] << " " << _middle[7] << " " << _mi ddle[8] << endl;
 //cout << "Observed LIMS mu: " << _observed[0] << " " << _observed[1] << " " << _observed[2] << " " << _observed[3] << " " << _observed[4] << " " << _observed[5] << " " << _observed[6] << " " << _observed[7 ] << " " << _observed[8] << endl;
 
 for(int i=0;i<n;i++){
   cout << _mzp[i] << " 1 " <<  _2siglow[i] << " " << _1siglow[i] << " " << _middle[i] << " " << _1sighigh[i] << " " << _2sighigh[i] << " " << _observed[i] << endl;
 }

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
for(i=0;i<n;i++){
  grshade1->SetPoint(i, _mzp[i], _1sighigh[i]);
  grshade1->SetPoint(n+i, _mzp[n-i-1], _1siglow[n-i-1]);
}
for(i=0;i<n;i++){
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
//TH2F * hframe = new TH2F("hframe", "", 10, 0, 2000, 10, 1E-2, 1E4);
//TH2F * hframe = new TH2F("hframe", "", 10, 100, 2000, 10, 5E-3, 10.);
TH2F * hframe = new TH2F("hframe", "", 10, 100, 2000, 10, 5E-3, 200.);
//hframe->GetXaxis()->SetTitleOffset(1.0);
//hframe->GetXaxis()->SetTitleSize(0.04);

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

//if (strncmp(channel.c_str(), "4mu", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi #mu#mu#mu#mu) [fb]");
//if (strncmp(channel.c_str(), "4e", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi eeee) [fb]");
//if (strncmp(channel.c_str(), "2e2mu", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z' #rightarrow A_{0}H #rightarrow #chi #chi ee#mu#mu) [fb]");
//if (strncmp(channel.c_str(), "4l", 10) == 0) hframe->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z'H #rightarrow #chi #chi llll) [fb]");
//hframe->GetYaxis()->SetTitle("#sigma_{95%CL} / #sigma_{theory}");
//hframe->GetYaxis()->SetTitleOffset(1.0);
//hframe->GetYaxis()->SetTitleSize(0.04);
//hframe->Draw();
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

//gPad->SetFrameLineWidth(2);
//gStyle->SetLineWidth(2);

gPad->RedrawAxis();

// Legend formatting
//TLegend *leg = new TLegend(0.7,0.65,0.85,0.85);
//TLegend *leg = new TLegend(0.15,0.2,0.35,0.4);
TLegend *leg = new TLegend(0.15,0.15,0.35,0.35);
//leg->SetFillStyle(0);
leg->SetFillColor(kWhite);
leg->SetBorderSize(0);
leg->AddEntry(gxsec, "Z^{'}_{Baryonic}: #sigma x BR", "L");
leg->AddEntry(gmiddle, "Expected limit", "L");
leg->AddEntry(grshade1, "#pm 1 #sigma", "F");
leg->AddEntry(grshade2, "#pm 2 #sigma", "F");
leg->AddEntry(gobserved, "Observed limit", "L");
leg->SetTextSize(0.032);
leg->Draw();

//TPaveText *leg0 = new TPaveText(0.3, 0.75, 0.6, 0.89, "NDC");
TPaveText *leg0 = new TPaveText(0.3, 0.71, 0.68, 0.85, "NDC");
leg0->SetTextSize(0.032);
leg0->SetTextFont(42);
leg0->SetFillColor(0);
leg0->SetBorderSize(0);
leg0->SetMargin(0.01);
leg0->SetTextAlign(12);
TString te1 = "Z'-baryonic, mono-H, H #rightarrow ZZ #rightarrow 4l";
leg0->AddText(0.1,0.8,te1);
TString te2 = "g_{q} = 1/3, g_{#chi} = 1";
leg0->AddText(0.1,0.45,te2);
TString te3 = "g_{HZ'Z'} = m_{Z'}, m_{#chi}= 1 GeV";
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
ll->Draw();


// Save plot
 char savepdf[50], saveeps[50], savepng[50];
sprintf(savepdf, "plots/sigma_limits_%s_ZpBaryonic.pdf", channel.c_str());
c->SaveAs(savepdf);
sprintf(saveeps, "plots/sigma_limits_%s_ZpBaryonic.eps", channel.c_str());
c->SaveAs(saveeps);
sprintf(savepng, "plots/sigma_limits_%s_ZpBaryonic.png", channel.c_str());
c->SaveAs(savepng);
/*
//mchi
//1      1      1      1      1       1     1      1      1      1
//mzp
//10     20     50     100    200    300    500    1000   2000   10000
//6.4062 7.9062 8.5312 7.7812 7.2188 6.7188 5.0469 3.4766 3.0078 3.4219
//mchi
//10     10     10     10     10     10     10     10     10     10
//mzp
//10     15     50     100    10000   
//7.9531 8.0938 8.4062 7.9688 3.4531
//mchi
//10     50     50     50     50     50     
//mzp
//10     50     95     200    300    10000
//6.2031 6.4688 7.1875 6.4688 6.7812 3.4531
//mchi
//150    150    150    150    150    150     
//mzp
//10     200    295    500    1000    10000
//4.0781 4.3281 4.8594 5.2344 3.5469 3.4531
//mchi
//500    500    500    500    500         
//mzp
//10     500    995    2000   10000    
//3.0078 2.9883 3.4219 2.9375 3.5781
//mchi
//1000   1000   1000   1000   1000   1000     
//mzp
//10     1000   1995   10000    
//2.9297 2.9141 3.0547 3.6406


Double_t _sig[36] = {6.4062, 7.9062, 8.5312, 7.7812, 7.2188, 6.7188, 5.0469, 3.4766, 3.0078, 3.4219, 7.9531, 8.0938, 8.4062, 7.9688, 3.4531, 6.2031, 6.4688, 7.1875, 6.4688, 6.7812, 3.4531, 4.0781, 4.3281, 4.8594, 5.2344, 3.5469, 3.4531, 3.0078, 2.9883, 3.4219, 2.9375, 3.5781, 2.9297, 2.9141, 3.0547, 3.6406};
for(int i=0;i<36;i++){
  _sig[i]  *= BR*PBtoFB;
}
Double_t _mzp2d[36] = {10, 20, 50, 100, 200, 300, 500, 1000, 2000, 10000, 10, 15, 50, 100, 10000, 10, 50, 95, 200, 300, 10000, 10, 200, 295, 500, 1000, 10000, 10, 500, 995, 2000, 10000, 10, 1000, 1995, 10000};
Double_t _ma0[36] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 50, 50, 50, 50, 50, 50, 150, 150, 150, 150, 150, 150, 500, 500, 500, 500, 500, 1000, 1000, 1000, 1000};

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
TGraph2D *g2d = new TGraph2D(36, _mzp2d, _ma0, _sig);
g2d->SetNpx(8);
g2d->SetNpy(6);
g2d->SetTitle("");
g2d->Draw("TEXTCOLZ");
gPad->Update();
g2d->GetXaxis()->SetTitle("m_{Z'} [GeV]");
g2d->GetXaxis()->SetTitleOffset(1.0);
g2d->GetXaxis()->SetTitleSize(0.04);
g2d->GetYaxis()->SetTitle("m_{#chi} [GeV]");
g2d->GetYaxis()->SetTitleOffset(1.0);
g2d->GetYaxis()->SetTitleSize(0.04);

TH1F *dummy = new TH1F("dummy", "", 100, 0, 100);
dummy->GetYaxis()->SetTitle("95% C.L. #sigma(pp #rightarrow Z'H #rightarrow #chi #chi llll) [fb]");
dummy->GetYaxis()->SetTitleSize(0.04);
dummy->GetYaxis()->SetTitleOffset(1.8);
dummy->GetXaxis()->SetLabelOffset(100.0);
dummy->Draw("Y+");
   pad2->Draw();
   pad2->cd();
   dummy->Draw("Y+");
g2d->Draw("TEXTCOLZ");
g2d->SetMarkerStyle(20);
gPad->Update();
//hframe1->Draw("SAME");
ll->Draw();
c1->SaveAs("plots/sigma_limits_2D_ZpBaryonic.png");

*/


// Write to file
char foutroot[50];
sprintf(foutroot,"plots/sigma_limits_%s_ZpBaryonic.root", channel.c_str());
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
