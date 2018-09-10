#!/usr/bin/env python
# -----------------------------------------------------------------------------
#  File:        MonoHiggsSelection.py
#  Usage:       python MonoHiggsSelection.py --channel 4mu
#  Description: Apply optimized event selection, including various machine learning
#               algorithm testing, printing out event yields and writing shape histograms
#               to a file for limit setting.
#  Created:     Nicola De Filippis
# -----------------------------------------------------------------------------
from ROOT import *
import numpy as np
import math
import argparse

# Convert ROOT TNtuple data structure to Python arrays
def get_data_from_mc(fmc):
  f = TFile.Open(fmc)
  t = f.Get("HZZ4LeptonsAnalysisReduced")
  event = []
  weight = []
  pfmet  = []
  mass4l = []
  mT     = []
  dphi   = []
  Dkin   = []
  cat    = []
  Ngood  = []
  Nbjets = []
  pfmet_JetEnUp = []
  pfmet_JetEnDn = []
  pfmet_ElectronEnUp = []
  pfmet_ElectronEnDn = []
  pfmet_MuonEnUp = []
  pfmet_MuonEnDn = []
  pfmet_JetResUp = []
  pfmet_JetResDn = []
  pfmet_UnclusteredEnUp = []
  pfmet_UnclusteredEnDn = []
  pfmet_PhotonEnUp = []
  pfmet_PhotonEnDn = []

  for evt in t:
    event.append(evt.f_event)
    weight.append(evt.f_weight)
    pfmet.append(evt.f_pfmet)
    mass4l.append(evt.f_mass4l)
    mT.append(evt.f_mT)
    dphi.append(evt.f_dphi)
    Dkin.append(evt.f_D_bkg_kin)
    cat.append(evt.f_category)
    Ngood.append(evt.f_Ngood)
    Nbjets.append(evt.f_Nbjets)
    pfmet_JetEnUp.append(evt.f_pfmet_JetEnUp)
    pfmet_JetEnDn.append(evt.f_pfmet_JetEnDn)
    pfmet_ElectronEnUp.append(evt.f_pfmet_ElectronEnUp)
    pfmet_ElectronEnDn.append(evt.f_pfmet_ElectronEnDn)
    pfmet_MuonEnUp.append(evt.f_pfmet_MuonEnUp)
    pfmet_MuonEnDn.append(evt.f_pfmet_MuonEnDn)
    pfmet_JetResUp.append(evt.f_pfmet_JetResUp)
    pfmet_JetResDn.append(evt.f_pfmet_JetResDn)
    pfmet_UnclusteredEnUp.append(evt.f_pfmet_UnclusteredEnUp)
    pfmet_UnclusteredEnDn.append(evt.f_pfmet_UnclusteredEnDn)
    pfmet_PhotonEnUp.append(evt.f_pfmet_PhotonEnUp)
    pfmet_PhotonEnDn.append(evt.f_pfmet_PhotonEnDn)

  f.Close()
  return (event, weight, pfmet, mass4l, mT, dphi, Dkin, cat, Ngood, Nbjets, pfmet_JetEnUp, pfmet_JetEnDn, pfmet_ElectronEnUp, pfmet_ElectronEnDn, pfmet_MuonEnUp, pfmet_MuonEnDn, pfmet_JetResUp, pfmet_JetResDn, pfmet_UnclusteredEnUp, pfmet_UnclusteredEnDn, pfmet_PhotonEnUp, pfmet_PhotonEnDn )

def get_data_from_data(fdata):
  f = TFile.Open(fdata)
  t = f.Get("HZZ4LeptonsAnalysisReduced")
  event = []
  weight = []
  pfmet  = []
  mass4l = []
  mT     = []
  dphi   = []
  Dkin   = []
  cat    = []
  Ngood  = []
  Nbjets = []  

  for evt in t:
    event.append(evt.f_event)
    weight.append(evt.f_weight)
    pfmet.append(evt.f_pfmet)
    mass4l.append(evt.f_mass4l)
    mT.append(evt.f_mT)
    dphi.append(evt.f_dphi)
    Dkin.append(evt.f_D_bkg_kin)
    cat.append(evt.f_category)
    Ngood.append(evt.f_Ngood)
    Nbjets.append(evt.f_Nbjets)
    
  f.Close()
  return (event, weight, pfmet, mass4l, mT, dphi, Dkin, cat, Ngood, Nbjets)



if __name__ == "__main__":
 
  # Parse command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('--channel', required=True, help='Decay channel: 4mu, 4e, or 2e2mu')
  args = parser.parse_args()

  # Read in list of data and simulation files
  flist = map(lambda x: x.split()[-1], open('filelist_' + args.channel + '_2016_Spring16_AN_Bari.txt').readlines()) 
  # Book histograms for shape analysis
  H1pfmet_D    = TH1F("H1pfmet_D", "", 10000, 0, 10000)
  H1pfmet_D.Sumw2()

  H1pfmet_wH   = TH1F("WH", "WH", 10000, 0, 10000)
  H1pfmet_wH.Sumw2()
  H1pfmet_wH_JetEnUp  = TH1F("WH_MET_JetEnUp", "WH_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_wH_JetEnUp.Sumw2()
  H1pfmet_wH_JetEnDown  = TH1F("WH_MET_JetEnDown", "WH_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_wH_JetEnDown.Sumw2()
  H1pfmet_wH_ElectronEnUp  = TH1F("WH_MET_ElectronEnUp", "WH_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_wH_ElectronEnUp.Sumw2()
  H1pfmet_wH_ElectronEnDown  = TH1F("WH_MET_ElectronEnDown", "WH_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_wH_ElectronEnDown.Sumw2()
  H1pfmet_wH_MuonEnUp  = TH1F("WH_MET_MuonEnUp", "WH_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_wH_MuonEnUp.Sumw2()
  H1pfmet_wH_MuonEnDown  = TH1F("WH_MET_MuonEnDown", "WH_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_wH_MuonEnDown.Sumw2()
  H1pfmet_wH_JetResUp  = TH1F("WH_MET_JetResUp", "WH_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_wH_JetResUp.Sumw2()
  H1pfmet_wH_JetResDown  = TH1F("WH_MET_JetResDown", "WH_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_wH_JetResDown.Sumw2()
  H1pfmet_wH_UnclusteredEnUp  = TH1F("WH_MET_UnclusteredEnUp", "WH_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_wH_UnclusteredEnUp.Sumw2()
  H1pfmet_wH_UnclusteredEnDown  = TH1F("WH_MET_UnclusteredEnDown", "WH_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_wH_UnclusteredEnDown.Sumw2()
  H1pfmet_wH_PhotonEnUp  = TH1F("WH_MET_PhotonEnUp", "WH_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_wH_PhotonEnUp.Sumw2()
  H1pfmet_wH_PhotonEnDown  = TH1F("WH_MET_PhotonEnDown", "WH_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_wH_PhotonEnDown.Sumw2()
  H1pfmet_wH_FakeUp  = TH1F("WH_MET_FakeUp", "WH_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_wH_FakeUp.Sumw2()
  H1pfmet_wH_FakeDown  = TH1F("WH_MET_FakeDown", "WH_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_wH_FakeDown.Sumw2()


  H1pfmet_ZH   = TH1F("ZH", "ZH", 10000, 0, 10000)
  H1pfmet_ZH.Sumw2()
  H1pfmet_ZH_JetEnUp  = TH1F("ZH_MET_JetEnUp", "ZH_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_ZH_JetEnUp.Sumw2()
  H1pfmet_ZH_JetEnDown  = TH1F("ZH_MET_JetEnDown", "ZH_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_ZH_JetEnDown.Sumw2()
  H1pfmet_ZH_ElectronEnUp  = TH1F("ZH_MET_ElectronEnUp", "ZH_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_ZH_ElectronEnUp.Sumw2()
  H1pfmet_ZH_ElectronEnDown  = TH1F("ZH_MET_ElectronEnDown", "ZH_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_ZH_ElectronEnDown.Sumw2()
  H1pfmet_ZH_MuonEnUp  = TH1F("ZH_MET_MuonEnUp", "ZH_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_ZH_MuonEnUp.Sumw2()
  H1pfmet_ZH_MuonEnDown  = TH1F("ZH_MET_MuonEnDown", "ZH_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_ZH_MuonEnDown.Sumw2()
  H1pfmet_ZH_JetResUp  = TH1F("ZH_MET_JetResUp", "ZH_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_ZH_JetResUp.Sumw2()
  H1pfmet_ZH_JetResDown  = TH1F("ZH_MET_JetResDown", "ZH_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_ZH_JetResDown.Sumw2()
  H1pfmet_ZH_UnclusteredEnUp  = TH1F("ZH_MET_UnclusteredEnUp", "ZH_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_ZH_UnclusteredEnUp.Sumw2()
  H1pfmet_ZH_UnclusteredEnDown  = TH1F("ZH_MET_UnclusteredEnDown", "ZH_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_ZH_UnclusteredEnDown.Sumw2()
  H1pfmet_ZH_PhotonEnUp  = TH1F("ZH_MET_PhotonEnUp", "ZH_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_ZH_PhotonEnUp.Sumw2()
  H1pfmet_ZH_PhotonEnDown  = TH1F("ZH_MET_PhotonEnDown", "ZH_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_ZH_PhotonEnDown.Sumw2()
  H1pfmet_ZH_FakeUp  = TH1F("ZH_MET_FakeUp", "ZH_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_ZH_FakeUp.Sumw2()
  H1pfmet_ZH_FakeDown  = TH1F("ZH_MET_FakeDown", "ZH_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_ZH_FakeDown.Sumw2()


  H1pfmet_ggH  = TH1F("ggH", "ggH", 10000, 0, 10000)
  H1pfmet_ggH.Sumw2()
  H1pfmet_ggH_JetEnUp  = TH1F("ggH_MET_JetEnUp", "ggH_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_ggH_JetEnUp.Sumw2()
  H1pfmet_ggH_JetEnDown  = TH1F("ggH_MET_JetEnDown", "ggH_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_ggH_JetEnDown.Sumw2()
  H1pfmet_ggH_ElectronEnUp  = TH1F("ggH_MET_ElectronEnUp", "ggH_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_ggH_ElectronEnUp.Sumw2()
  H1pfmet_ggH_ElectronEnDown  = TH1F("ggH_MET_ElectronEnDown", "ggH_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_ggH_ElectronEnDown.Sumw2()
  H1pfmet_ggH_MuonEnUp  = TH1F("ggH_MET_MuonEnUp", "ggH_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_ggH_MuonEnUp.Sumw2()
  H1pfmet_ggH_MuonEnDown  = TH1F("ggH_MET_MuonEnDown", "ggH_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_ggH_MuonEnDown.Sumw2()
  H1pfmet_ggH_JetResUp  = TH1F("ggH_MET_JetResUp", "ggH_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_ggH_JetResUp.Sumw2()
  H1pfmet_ggH_JetResDown  = TH1F("ggH_MET_JetResDown", "ggH_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_ggH_JetResDown.Sumw2()
  H1pfmet_ggH_UnclusteredEnUp  = TH1F("ggH_MET_UnclusteredEnUp", "ggH_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_ggH_UnclusteredEnUp.Sumw2()
  H1pfmet_ggH_UnclusteredEnDown  = TH1F("ggH_MET_UnclusteredEnDown", "ggH_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_ggH_UnclusteredEnDown.Sumw2()
  H1pfmet_ggH_PhotonEnUp  = TH1F("ggH_MET_PhotonEnUp", "ggH_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_ggH_PhotonEnUp.Sumw2()
  H1pfmet_ggH_PhotonEnDown  = TH1F("ggH_MET_PhotonEnDown", "ggH_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_ggH_PhotonEnDown.Sumw2()
  H1pfmet_ggH_FakeUp  = TH1F("ggH_MET_FakeUp", "ggH_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_ggH_FakeUp.Sumw2()
  H1pfmet_ggH_FakeDown  = TH1F("ggH_MET_FakeDown", "ggH_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_ggH_FakeDown.Sumw2()


  H1pfmet_VBFH  = TH1F("qqH", "qqH", 10000, 0, 10000)
  H1pfmet_VBFH.Sumw2()
  H1pfmet_VBFH_JetEnUp  = TH1F("qqH_MET_JetEnUp", "qqH_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_VBFH_JetEnUp.Sumw2()
  H1pfmet_VBFH_JetEnDown  = TH1F("qqH_MET_JetEnDown", "qqH_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_VBFH_JetEnDown.Sumw2()
  H1pfmet_VBFH_ElectronEnUp  = TH1F("qqH_MET_ElectronEnUp", "qqH_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_VBFH_ElectronEnUp.Sumw2()
  H1pfmet_VBFH_ElectronEnDown  = TH1F("qqH_MET_ElectronEnDown", "qqH_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_VBFH_ElectronEnDown.Sumw2()
  H1pfmet_VBFH_MuonEnUp  = TH1F("qqH_MET_MuonEnUp", "qqH_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_VBFH_MuonEnUp.Sumw2()
  H1pfmet_VBFH_MuonEnDown  = TH1F("qqH_MET_MuonEnDown", "qqH_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_VBFH_MuonEnDown.Sumw2()
  H1pfmet_VBFH_JetResUp  = TH1F("qqH_MET_JetResUp", "qqH_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_VBFH_JetResUp.Sumw2()
  H1pfmet_VBFH_JetResDown  = TH1F("qqH_MET_JetResDown", "qqH_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_VBFH_JetResDown.Sumw2()
  H1pfmet_VBFH_UnclusteredEnUp  = TH1F("qqH_MET_UnclusteredEnUp", "qqH_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_VBFH_UnclusteredEnUp.Sumw2()
  H1pfmet_VBFH_UnclusteredEnDown  = TH1F("qqH_MET_UnclusteredEnDown", "qqH_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_VBFH_UnclusteredEnDown.Sumw2()
  H1pfmet_VBFH_PhotonEnUp  = TH1F("qqH_MET_PhotonEnUp", "qqH_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_VBFH_PhotonEnUp.Sumw2()
  H1pfmet_VBFH_PhotonEnDown  = TH1F("qqH_MET_PhotonEnDown", "qqH_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_VBFH_PhotonEnDown.Sumw2()
  H1pfmet_VBFH_FakeUp  = TH1F("qqH_MET_FakeUp", "qqH_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_VBFH_FakeUp.Sumw2()
  H1pfmet_VBFH_FakeDown  = TH1F("qqH_MET_FakeDown", "qqH_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_VBFH_FakeDown.Sumw2()


  H1pfmet_ttH  = TH1F("ttH", "ttH", 10000, 0, 10000)
  H1pfmet_ttH.Sumw2()
  H1pfmet_ttH_JetEnUp  = TH1F("ttH_MET_JetEnUp", "ttH_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_ttH_JetEnUp.Sumw2()
  H1pfmet_ttH_JetEnDown  = TH1F("ttH_MET_JetEnDown", "ttH_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_ttH_JetEnDown.Sumw2()
  H1pfmet_ttH_ElectronEnUp  = TH1F("ttH_MET_ElectronEnUp", "ttH_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_ttH_ElectronEnUp.Sumw2()
  H1pfmet_ttH_ElectronEnDown  = TH1F("ttH_MET_ElectronEnDown", "ttH_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_ttH_ElectronEnDown.Sumw2()
  H1pfmet_ttH_MuonEnUp  = TH1F("ttH_MET_MuonEnUp", "ttH_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_ttH_MuonEnUp.Sumw2()
  H1pfmet_ttH_MuonEnDown  = TH1F("ttH_MET_MuonEnDown", "ttH_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_ttH_MuonEnDown.Sumw2()
  H1pfmet_ttH_JetResUp  = TH1F("ttH_MET_JetResUp", "ttH_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_ttH_JetResUp.Sumw2()
  H1pfmet_ttH_JetResDown  = TH1F("ttH_MET_JetResDown", "ttH_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_ttH_JetResDown.Sumw2()
  H1pfmet_ttH_UnclusteredEnUp  = TH1F("ttH_MET_UnclusteredEnUp", "ttH_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_ttH_UnclusteredEnUp.Sumw2()
  H1pfmet_ttH_UnclusteredEnDown  = TH1F("ttH_MET_UnclusteredEnDown", "ttH_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_ttH_UnclusteredEnDown.Sumw2()
  H1pfmet_ttH_PhotonEnUp  = TH1F("ttH_MET_PhotonEnUp", "ttH_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_ttH_PhotonEnUp.Sumw2()
  H1pfmet_ttH_PhotonEnDown  = TH1F("ttH_MET_PhotonEnDown", "ttH_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_ttH_PhotonEnDown.Sumw2()
  H1pfmet_ttH_FakeUp  = TH1F("ttH_MET_FakeUp", "ttH_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_ttH_FakeUp.Sumw2()
  H1pfmet_ttH_FakeDown  = TH1F("ttH_MET_FakeDown", "ttH_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_ttH_FakeDown.Sumw2()


  H1pfmet_HWW  = TH1F("HWW", "HWW", 10000, 0, 10000)
  H1pfmet_HWW.Sumw2()
  H1pfmet_HWW_JetEnUp  = TH1F("HWW_MET_JetEnUp", "HWW_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_HWW_JetEnUp.Sumw2()
  H1pfmet_HWW_JetEnDown  = TH1F("HWW_MET_JetEnDown", "HWW_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_HWW_JetEnDown.Sumw2()
  H1pfmet_HWW_ElectronEnUp  = TH1F("HWW_MET_ElectronEnUp", "HWW_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_HWW_ElectronEnUp.Sumw2()
  H1pfmet_HWW_ElectronEnDown  = TH1F("HWW_MET_ElectronEnDown", "HWW_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_HWW_ElectronEnDown.Sumw2()
  H1pfmet_HWW_MuonEnUp  = TH1F("HWW_MET_MuonEnUp", "HWW_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_HWW_MuonEnUp.Sumw2()
  H1pfmet_HWW_MuonEnDown  = TH1F("HWW_MET_MuonEnDown", "HWW_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_HWW_MuonEnDown.Sumw2()
  H1pfmet_HWW_JetResUp  = TH1F("HWW_MET_JetResUp", "HWW_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_HWW_JetResUp.Sumw2()
  H1pfmet_HWW_JetResDown  = TH1F("HWW_MET_JetResDown", "HWW_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_HWW_JetResDown.Sumw2()
  H1pfmet_HWW_UnclusteredEnUp  = TH1F("HWW_MET_UnclusteredEnUp", "HWW_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_HWW_UnclusteredEnUp.Sumw2()
  H1pfmet_HWW_UnclusteredEnDown  = TH1F("HWW_MET_UnclusteredEnDown", "HWW_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_HWW_UnclusteredEnDown.Sumw2()
  H1pfmet_HWW_PhotonEnUp  = TH1F("HWW_MET_PhotonEnUp", "HWW_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_HWW_PhotonEnUp.Sumw2()
  H1pfmet_HWW_PhotonEnDown  = TH1F("HWW_MET_PhotonEnDown", "HWW_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_HWW_PhotonEnDown.Sumw2()
  H1pfmet_HWW_FakeUp  = TH1F("HWW_MET_FakeUp", "HWW_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_HWW_FakeUp.Sumw2()
  H1pfmet_HWW_FakeDown  = TH1F("HWW_MET_FakeDown", "HWW_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_HWW_FakeDown.Sumw2()


  H1pfmet_GGZZ = TH1F("ggZZ", "ggZZ", 10000, 0, 10000)
  H1pfmet_GGZZ.Sumw2()
  H1pfmet_GGZZ_JetEnUp  = TH1F("ggZZ_MET_JetEnUp", "ggZZ_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_GGZZ_JetEnUp.Sumw2()
  H1pfmet_GGZZ_JetEnDown  = TH1F("ggZZ_MET_JetEnDown", "ggZZ_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_GGZZ_JetEnDown.Sumw2()
  H1pfmet_GGZZ_ElectronEnUp  = TH1F("ggZZ_MET_ElectronEnUp", "ggZZ_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_GGZZ_ElectronEnUp.Sumw2()
  H1pfmet_GGZZ_ElectronEnDown  = TH1F("ggZZ_MET_ElectronEnDown", "ggZZ_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_GGZZ_ElectronEnDown.Sumw2()
  H1pfmet_GGZZ_MuonEnUp  = TH1F("ggZZ_MET_MuonEnUp", "ggZZ_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_GGZZ_MuonEnUp.Sumw2()
  H1pfmet_GGZZ_MuonEnDown  = TH1F("ggZZ_MET_MuonEnDown", "ggZZ_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_GGZZ_MuonEnDown.Sumw2()
  H1pfmet_GGZZ_JetResUp  = TH1F("ggZZ_MET_JetResUp", "ggZZ_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_GGZZ_JetResUp.Sumw2()
  H1pfmet_GGZZ_JetResDown  = TH1F("ggZZ_MET_JetResDown", "ggZZ_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_GGZZ_JetResDown.Sumw2()
  H1pfmet_GGZZ_UnclusteredEnUp  = TH1F("ggZZ_MET_UnclusteredEnUp", "ggZZ_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_GGZZ_UnclusteredEnUp.Sumw2()
  H1pfmet_GGZZ_UnclusteredEnDown  = TH1F("ggZZ_MET_UnclusteredEnDown", "ggZZ_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_GGZZ_UnclusteredEnDown.Sumw2()
  H1pfmet_GGZZ_PhotonEnUp  = TH1F("ggZZ_MET_PhotonEnUp", "ggZZ_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_GGZZ_PhotonEnUp.Sumw2()
  H1pfmet_GGZZ_PhotonEnDown  = TH1F("ggZZ_MET_PhotonEnDown", "ggZZ_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_GGZZ_PhotonEnDown.Sumw2()
  H1pfmet_GGZZ_FakeUp  = TH1F("ggZZ_MET_FakeUp", "ggZZ_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_GGZZ_FakeUp.Sumw2()
  H1pfmet_GGZZ_FakeDown  = TH1F("ggZZ_MET_FakeDown", "ggZZ_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_GGZZ_FakeDown.Sumw2()


  H1pfmet_QQZZ = TH1F("qqZZ", "qqZZ", 10000, 0, 10000)
  H1pfmet_QQZZ.Sumw2()
  H1pfmet_QQZZ_JetEnUp  = TH1F("qqZZ_MET_JetEnUp", "qqZZ_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_QQZZ_JetEnUp.Sumw2()
  H1pfmet_QQZZ_JetEnDown  = TH1F("qqZZ_MET_JetEnDown", "qqZZ_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_QQZZ_JetEnDown.Sumw2()
  H1pfmet_QQZZ_sElectronEnUp  = TH1F("qqZZ_MET_ElectronEnUp", "qqZZ_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_QQZZ_sElectronEnUp.Sumw2()
  H1pfmet_QQZZ_sElectronEnDown  = TH1F("qqZZ_MET_ElectronEnDown", "qqZZ_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_QQZZ_sElectronEnDown.Sumw2()
  H1pfmet_QQZZ_MuonEnUp  = TH1F("qqZZ_MET_MuonEnUp", "qqZZ_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_QQZZ_MuonEnUp.Sumw2()
  H1pfmet_QQZZ_MuonEnDown  = TH1F("qqZZ_MET_MuonEnDown", "qqZZ_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_QQZZ_MuonEnDown.Sumw2()
  H1pfmet_QQZZ_JetResUp  = TH1F("qqZZ_MET_JetResUp", "qqZZ_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_QQZZ_JetResUp.Sumw2()
  H1pfmet_QQZZ_JetResDown  = TH1F("qqZZ_MET_JetResDown", "qqZZ_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_QQZZ_JetResDown.Sumw2()
  H1pfmet_QQZZ_UnclusteredEnUp  = TH1F("qqZZ_MET_UnclusteredEnUp", "qqZZ_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_QQZZ_UnclusteredEnUp.Sumw2()
  H1pfmet_QQZZ_UnclusteredEnDown  = TH1F("qqZZ_MET_UnclusteredEnDown", "qqZZ_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_QQZZ_UnclusteredEnDown.Sumw2()
  H1pfmet_QQZZ_PhotonEnUp  = TH1F("qqZZ_MET_PhotonEnUp", "qqZZ_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_QQZZ_PhotonEnUp.Sumw2()
  H1pfmet_QQZZ_PhotonEnDown  = TH1F("qqZZ_MET_PhotonEnDown", "qqZZ_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_QQZZ_PhotonEnDown.Sumw2()
  H1pfmet_QQZZ_FakeUp  = TH1F("qqZZ_MET_FakeUp", "qqZZ_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_QQZZ_FakeUp.Sumw2()
  H1pfmet_QQZZ_FakeDown  = TH1F("qqZZ_MET_FakeDown", "qqZZ_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_QQZZ_FakeDown.Sumw2()


  H1pfmet_VVV = TH1F("VVV", "VVV", 10000, 0, 10000)
  H1pfmet_VVV.Sumw2()
  H1pfmet_VVV_JetEnUp  = TH1F("VVV_MET_JetEnUp", "VVV_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_VVV_JetEnUp.Sumw2()
  H1pfmet_VVV_JetEnDown  = TH1F("VVV_MET_JetEnDown", "VVV_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_VVV_JetEnDown.Sumw2()
  H1pfmet_VVV_ElectronEnUp  = TH1F("VVV_MET_ElectronEnUp", "VVV_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_VVV_ElectronEnUp.Sumw2()
  H1pfmet_VVV_ElectronEnDown  = TH1F("VVV_MET_ElectronEnDown", "VVV_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_VVV_ElectronEnDown.Sumw2()
  H1pfmet_VVV_MuonEnUp  = TH1F("VVV_MET_MuonEnUp", "VVV_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_VVV_MuonEnUp.Sumw2()
  H1pfmet_VVV_MuonEnDown  = TH1F("VVV_MET_MuonEnDown", "VVV_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_VVV_MuonEnDown.Sumw2()
  H1pfmet_VVV_JetResUp  = TH1F("VVV_MET_JetResUp", "VVV_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_VVV_JetResUp.Sumw2()
  H1pfmet_VVV_JetResDown  = TH1F("VVV_MET_JetResDown", "VVV_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_VVV_JetResDown.Sumw2()  
  H1pfmet_VVV_UnclusteredEnUp  = TH1F("VVV_MET_UnclusteredEnUp", "VVV_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_VVV_UnclusteredEnUp.Sumw2()
  H1pfmet_VVV_UnclusteredEnDown  = TH1F("VVV_MET_UnclusteredEnDown", "VV_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_VVV_UnclusteredEnDown.Sumw2()
  H1pfmet_VVV_PhotonEnUp  = TH1F("VVV_MET_PhotonEnUp", "VVV_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_VVV_PhotonEnUp.Sumw2()
  H1pfmet_VVV_PhotonEnDown  = TH1F("VVV_MET_PhotonEnDown", "VVV_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_VVV_PhotonEnDown.Sumw2()
  H1pfmet_VVV_FakeUp  = TH1F("VVV_MET_FakeUp", "VVV_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_VVV_FakeUp.Sumw2()
  H1pfmet_VVV_FakeDown  = TH1F("VVV_MET_FakeDown", "VVV_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_VVV_FakeDown.Sumw2()


  H1pfmet_TTV = TH1F("TTV", "TTV", 10000, 0, 10000)
  H1pfmet_TTV.Sumw2()
  H1pfmet_TTV_JetEnUp  = TH1F("TTV_MET_JetEnUp", "TTV_MET_JetEnUp", 10000, 0, 10000)
  H1pfmet_TTV_JetEnUp.Sumw2()
  H1pfmet_TTV_JetEnDown  = TH1F("TTV_MET_JetEnDown", "TTV_MET_JetEnDown", 10000, 0, 10000)
  H1pfmet_TTV_JetEnDown.Sumw2()
  H1pfmet_TTV_ElectronEnUp  = TH1F("TTV_MET_ElectronEnUp", "TTV_MET_ElectronEnUp", 10000, 0, 10000)
  H1pfmet_TTV_ElectronEnUp.Sumw2()
  H1pfmet_TTV_ElectronEnDown  = TH1F("TTV_MET_ElectronEnDown", "TTV_MET_ElectronEnDown", 10000, 0, 10000)
  H1pfmet_TTV_ElectronEnDown.Sumw2()
  H1pfmet_TTV_MuonEnUp  = TH1F("TTV_MET_MuonEnUp", "TTV_MET_MuonEnUp", 10000, 0, 10000)
  H1pfmet_TTV_MuonEnUp.Sumw2()
  H1pfmet_TTV_MuonEnDown  = TH1F("TTV_MET_MuonEnDown", "TTV_MET_MuonEnDown", 10000, 0, 10000)
  H1pfmet_TTV_MuonEnDown.Sumw2()
  H1pfmet_TTV_JetResUp  = TH1F("TTV_MET_JetResUp", "TTV_MET_JetResUp", 10000, 0, 10000)
  H1pfmet_TTV_JetResUp.Sumw2()
  H1pfmet_TTV_JetResDown  = TH1F("TTV_MET_JetResDown", "TTV_MET_JetResDown", 10000, 0, 10000)
  H1pfmet_TTV_JetResDown.Sumw2()
  H1pfmet_TTV_UnclusteredEnUp  = TH1F("TTV_MET_UnclusteredEnUp", "TTV_MET_UnclusteredEnUp", 10000, 0, 10000)
  H1pfmet_TTV_UnclusteredEnUp.Sumw2()
  H1pfmet_TTV_UnclusteredEnDown  = TH1F("TTV_MET_UnclusteredEnDown", "TTV_MET_UnclusteredEnDown", 10000, 0, 10000)
  H1pfmet_TTV_UnclusteredEnDown.Sumw2()
  H1pfmet_TTV_PhotonEnUp  = TH1F("TTV_MET_PhotonEnUp", "TTV_MET_PhotonEnUp", 10000, 0, 10000)
  H1pfmet_TTV_PhotonEnUp.Sumw2()
  H1pfmet_TTV_PhotonEnDown  = TH1F("TTV_MET_PhotonEnDown", "TTV_MET_PhotonEnDown", 10000, 0, 10000)
  H1pfmet_TTV_PhotonEnDown.Sumw2()
  H1pfmet_TTV_FakeUp  = TH1F("TTV_MET_FakeUp", "TTV_MET_FakeUp", 10000, 0, 10000)
  H1pfmet_TTV_FakeUp.Sumw2()
  H1pfmet_TTV_FakeDown  = TH1F("TTV_MET_FakeDown", "TTV_MET_FakeDown", 10000, 0, 10000)
  H1pfmet_TTV_FakeDown.Sumw2()


  if (args.channel=='4mu' or args.channel=='4e'):
    print 'This is ' + args.channel
    f1 = TFile.Open("/lustre/cms/store/user/defilip/MonoHiggs/80X/histos" + args.channel + "_25ns/Final_Estimation_" + args.channel + "_data_miniAOD_final_monoH3.root")
  elif args.channel=='2e2mu':
    print 'This is not 4e or 4mu but ' + args.channel
    f1 = TFile.Open("/lustre/cms/store/user/defilip/MonoHiggs/80X/histos" + args.channel + "_25ns/Final_Estimation_" + args.channel + "_2mu2e_data_miniAOD_final_monoH3.root")

  H1pfmet_ZX   = TH1F("ZX", "ZX", 10000, 0, 10000)
  #H1pfmet_ZX = f1.Get("h_MET_3P1F_2P2F")
  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX)
  #H1pfmet_ZX.Sumw2()
  err2_ZX = 0;
  for i in range(0, H1pfmet_ZX.GetXaxis().GetNbins()):
    err2_ZX += H1pfmet_ZX.GetBinError(i)**2;
  
  if (args.channel=='4mu' or args.channel=='4e'):
    print 'This is ' + args.channel
    print 'Sample name ' + args.channel + 'channel: ' + '/lustre/cms/store/user/defilip/MonoHiggs/80X/histos' + args.channel + '_25ns/Final_Estimation_' + args.channel + '_data_miniAOD_final_monoH3.root' + ' N Entries: ' + str(H1pfmet_ZX.GetEntries()) + ' Yield: ' + str(H1pfmet_ZX.Integral()) + ' Error: ' + str(math.sqrt(err2_ZX))  
  elif args.channel=='2e2mu':
    print 'This is not 4e or 4mu but ' + args.channel
    print 'Sample name ' + args.channel + 'channel: ' + '/lustre/cms/store/user/defilip/MonoHiggs/80X/histos' + args.channel + '_25ns/Final_Estimation_' + args.channel + '_2mu2e_data_miniAOD_final_monoH3.root' + ' N Entries: ' + str(H1pfmet_ZX.GetEntries()) + ' Yield: ' + str(H1pfmet_ZX.Integral()) + ' Error: ' + str(math.sqrt(err2_ZX))


#  H1pfmet_ZX_JetEnUp   = TH1F("ZX_JetEnUp", "ZX_JetEnUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_JetEnUp)
#  #H1pfmet_ZX_JetEnUp.Sumw2()
#  H1pfmet_ZX_JetEnDown   = TH1F("ZX_JetEnDown", "ZX_JetEnDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_JetEnDown)
#  #H1pfmet_ZX_JetEnDown.Sumw2()
#  H1pfmet_ZX_ElectronEnUp   = TH1F("ZX_ElectronEnUp", "ZX_ElectronEnUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_ElectronEnUp)
#  #H1pfmet_ZX_ElectronEnUp.Sumw2()
#  H1pfmet_ZX_ElectronEnDown   = TH1F("ZX_ElectronEnDown", "ZX_ElectronEnDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_ElectronEnDown)
#  #H1pfmet_ZX_ElectronEnDown.Sumw2()
#  H1pfmet_ZX_MuonEnUp   = TH1F("ZX_MuonEnUp", "ZX_MuonEnUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_MuonEnUp)
#  #H1pfmet_ZX_MuonEnUp.Sumw2()
#  H1pfmet_ZX_MuonEnDown   = TH1F("ZX_MuonEnDown", "ZX_MuonEnDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_MuonEnDown)
#  #H1pfmet_ZX_MuonEnDown.Sumw2()
#  H1pfmet_ZX_JetResUp   = TH1F("ZX_JetResUp", "ZX_JetResUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_JetResUp)
#  #H1pfmet_ZX_JetResUp.Sumw2()
#  H1pfmet_ZX_JetResDown   = TH1F("ZX_JetResDown", "ZX_JetResDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_JetResDown)
#  H1pfmet_ZX_UnclusteredEnUp   = TH1F("ZX_UnclusteredEnUp", "ZX_UnclusteredEnUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_UnclusteredEnUp)
#  #H1pfmet_ZX_UnclusteredEnUp.Sumw2()
#  H1pfmet_ZX_UnclusteredEnDown   = TH1F("ZX_UnclusteredEnDown", "ZX_UnclusteredEnDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_UnclusteredEnDown)
#  #H1pfmet_ZX_UnclusteredEnDown.Sumw2()
#  H1pfmet_ZX_PhotonEnUp   = TH1F("ZX_PhotonEnUp", "ZX_PhotonEnUp", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_PhotonEnUp)
#  #H1pfmet_ZX_PhotonEnUp.Sumw2()
#  H1pfmet_ZX_PhotonEnDown   = TH1F("ZX_PhotonEnDown", "ZX_PhotonEnDown", 10000, 0, 10000)
#  f1.GetObject("h_MET_3P1F_2P2F",H1pfmet_ZX_PhotonEnDown)
#  #H1pfmet_ZX_PhotonEnDown.Sumw2()

  # Fake MET weight
  # f_fake = TFile.Open("Data_MC_Ratio_CR_2p2f.root")
  # f_fake = TFile.Open("Data_MC_Ratio_off4lpeak_2p2f_test.root")
  # h_fake = f_fake.Get("hPFMET_MMMM_AI_AI_Step2_rev")
  #  f_fake = TFile.Open("Data_MC_Ratio_OS_SS_test_full_range.root")

  h_fake   = TH1F("h_fake", "h_fake", 10000, 0, 10000)
  f_fake = TFile.Open("Data_MC_Ratio_OS_SS_test_full_range.root")
  h_fake = f_fake.Get("htotalHistoRatio")
  
  H1pfmet_ZX_FakeUp   = TH1F("ZX_FakeUp", "ZX_FakeUp", 10000, 0, 10000)
  H1pfmet_ZX_FakeDown = TH1F("ZX_FakeDown", "ZX_FakeDown", 10000, 0, 10000)

  print H1pfmet_ZX.GetXaxis().GetNbins()

  for iii in range(0, H1pfmet_ZX.GetXaxis().GetNbins()):
    fake_ZX_weight=h_fake.GetBinContent(iii)
    # print h_fake.GetBinContent(iii)
    if fake_ZX_weight==0.0: fake_ZX_weight=1.
    H1pfmet_ZX_FakeUp.Fill(H1pfmet_ZX.GetBinContent(iii), fake_ZX_weight)
    H1pfmet_ZX_FakeDown.Fill(H1pfmet_ZX.GetBinContent(iii), (-fake_ZX_weight))
  
  integralZXUp=H1pfmet_ZX_FakeUp.Integral()
  H1pfmet_ZX_FakeUp.Scale(H1pfmet_ZX.Integral()/integralZXUp)
  integralZXDown=H1pfmet_ZX_FakeDown.Integral()
  H1pfmet_ZX_FakeDown.Scale(H1pfmet_ZX.Integral()/integralZXDown)  

  # print 'Weight histo for fake MET in CR, bin1= ', h_fake.GetBinContent(1)
 

  # Loop through input files, testing machine learning algorithm and applying signal region selection
  for f in flist:
    
    # Get Data
    if 'Run2016' in f: 
      event, weight, pfmet, mass4l, mT, dphi, Dkin, cat, Ngood, Nbjets = get_data_from_data(f)
    else:
      event, weight, pfmet, mass4l, mT, dphi, Dkin, cat, Ngood, Nbjets, pfmet_JetEnUp, pfmet_JetEnDn,  pfmet_ElectronEnUp, pfmet_ElectronEnDn, pfmet_MuonEnUp, pfmet_MuonEnDn, pfmet_JetResUp, pfmet_JetResDn, pfmet_UnclusteredEnUp, pfmet_UnclusteredEnDn, pfmet_PhotonEnUp, pfmet_PhotonEnDn = get_data_from_mc(f)

   
    # Book histograms for Monte Carlo simulation samples
    H1pfmet = TH1F("H1pfmet", "H1pfmet", 10000, 0, 10000)
    H1pfmet.Sumw2()

    if 'Run2016' not in f:
      H1pfmet_JetEnUp = TH1F("H1pfmet_JetEnUp", "H1pfmet_JetEnUp", 10000, 0, 10000)
      H1pfmet_JetEnUp.Sumw2()
      H1pfmet_JetEnDown = TH1F("H1pfmet_JetEnDown", "H1pfmet_JetEnDown", 10000, 0, 10000)  
      H1pfmet_JetEnDown.Sumw2()
      H1pfmet_ElectronEnUp = TH1F("H1pfmet_ElectronEnUp", "H1pfmet_ElectronEnUp", 10000, 0, 10000)
      H1pfmet_ElectronEnUp.Sumw2()
      H1pfmet_ElectronEnDown = TH1F("H1pfmet_ElectronEnDown", "H1pfmet_ElectronEnDown", 10000, 0, 10000)  
      H1pfmet_ElectronEnDown.Sumw2()
      H1pfmet_MuonEnUp = TH1F("H1pfmet_MuonEnUp", "H1pfmet_MuonEnUp", 10000, 0, 10000)
      H1pfmet_MuonEnUp.Sumw2()
      H1pfmet_MuonEnDown = TH1F("H1pfmet_MuonEnDown", "H1pfmet_MuonEnDown", 10000, 0, 10000)  
      H1pfmet_MuonEnDown.Sumw2()
      H1pfmet_JetResUp = TH1F("H1pfmet_JetResUp", "H1pfmet_JetResUp", 10000, 0, 10000)
      H1pfmet_JetResUp.Sumw2()
      H1pfmet_JetResDown = TH1F("H1pfmet_JetResDown", "H1pfmet_JetResDown", 10000, 0, 10000)  
      H1pfmet_JetResDown.Sumw2()
      H1pfmet_UnclusteredEnUp = TH1F("H1pfmet_UnclusteredEnUp", "H1pfmet_UnclusteredEnUp", 10000, 0, 10000)
      H1pfmet_UnclusteredEnUp.Sumw2()
      H1pfmet_UnclusteredEnDown = TH1F("H1pfmet_UnclusteredEnDown", "H1pfmet_UnclusteredEnDown", 10000, 0, 10000)  
      H1pfmet_UnclusteredEnDown.Sumw2()
      H1pfmet_PhotonEnUp = TH1F("H1pfmet_PhotonEnUp", "H1pfmet_PhotonEnUp", 10000, 0, 10000)
      H1pfmet_PhotonEnUp.Sumw2()
      H1pfmet_PhotonEnDown = TH1F("H1pfmet_PhotonEnDown", "H1pfmet_PhotonEnDown", 10000, 0, 10000)  
      H1pfmet_PhotonEnDown.Sumw2() 
      H1pfmet_FakeUp = TH1F("H1pfmet_FakeUp", "H1pfmet_FakeUp", 10000, 0, 10000)
      H1pfmet_FakeUp.Sumw2()
      H1pfmet_FakeDn = TH1F("H1pfmet_FakeDn", "H1pfmet_FakeDn", 10000, 0, 10000)
      H1pfmet_FakeDn.Sumw2()


    # Apply selection, filling histograms before and after
    for i in range(0, len(event)):

      # Step 1: MonoHiggs selection
      if Ngood[i] != 4: continue
      if Nbjets[i] > 1: continue
      #if pfmet[i] < 60: continue
      if np.abs(mass4l[i] - 125.) > 10.: continue
    
      H1pfmet.Fill(pfmet[i], weight[i])

      if 'Run2016' not in f:
        binx = h_fake.GetXaxis().FindBin(pfmet[i])
        # print ' bin x= ', binx, ' ', h_fake.GetBinContent(binx)
        fake_weight=h_fake.GetBinContent(binx)
        if fake_weight==0.0: fake_weight=1.
        # print ' bin x new= ', binx, ' ', fake_weight
        H1pfmet_FakeUp.Fill(pfmet[i],weight[i]*fake_weight)
        H1pfmet_FakeDn.Fill(pfmet[i],weight[i]*(-fake_weight))

        H1pfmet_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])   
        H1pfmet_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])   
        H1pfmet_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_JetResDown.Fill(pfmet_JetResDn[i], weight[i])   
        H1pfmet_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])   
        H1pfmet_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])   

      if 'Run2016' in f: 
        H1pfmet_D.Fill(pfmet[i], weight[i])
      elif ('WminusH' in f) or ('WplusH' in f):
        H1pfmet_wH.Fill(pfmet[i], weight[i])
        H1pfmet_wH_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_wH_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])           
        H1pfmet_wH_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_wH_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])   
        H1pfmet_wH_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_wH_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i])  
        H1pfmet_wH_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_wH_JetResDown.Fill(pfmet_JetResDn[i], weight[i]) 
        H1pfmet_wH_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_wH_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])  
        H1pfmet_wH_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_wH_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])   
        H1pfmet_wH_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_wH_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif 'ZH' in f:
        H1pfmet_ZH.Fill(pfmet[i], weight[i])
        H1pfmet_ZH_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_ZH_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])         
        H1pfmet_ZH_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_ZH_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_ZH_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_ZH_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_ZH_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_ZH_JetResDown.Fill(pfmet_JetResDn[i], weight[i])  
        H1pfmet_ZH_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_ZH_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_ZH_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_ZH_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])
        H1pfmet_ZH_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_ZH_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif 'GluGluHToZZTo4L' in f:
        H1pfmet_ggH.Fill(pfmet[i], weight[i])
        H1pfmet_ggH_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_ggH_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])        
        H1pfmet_ggH_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_ggH_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_ggH_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_ggH_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i])
        H1pfmet_ggH_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_ggH_JetResDown.Fill(pfmet_JetResDn[i], weight[i])
        H1pfmet_ggH_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_ggH_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_ggH_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_ggH_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_ggH_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_ggH_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif 'VBF_HToZZTo4L' in f:
        H1pfmet_VBFH.Fill(pfmet[i], weight[i])
        H1pfmet_VBFH_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_VBFH_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])   
        H1pfmet_VBFH_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_VBFH_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_VBFH_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_VBFH_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i])  
        H1pfmet_VBFH_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_VBFH_JetResDown.Fill(pfmet_JetResDn[i], weight[i])
        H1pfmet_VBFH_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_VBFH_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_VBFH_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_VBFH_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_VBFH_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_VBFH_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif 'ttH' in f:
        H1pfmet_ttH.Fill(pfmet[i], weight[i])
        H1pfmet_ttH_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_ttH_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])   
        H1pfmet_ttH_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_ttH_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])   
        H1pfmet_ttH_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_ttH_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_ttH_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_ttH_JetResDown.Fill(pfmet_JetResDn[i], weight[i])
        H1pfmet_ttH_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_ttH_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_ttH_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_ttH_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_ttH_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_ttH_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif 'HToWW' in f:
        H1pfmet_HWW.Fill(pfmet[i], weight[i])
        H1pfmet_HWW_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_HWW_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i]) 
        H1pfmet_HWW_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_HWW_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_HWW_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_HWW_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_HWW_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_HWW_JetResDown.Fill(pfmet_JetResDn[i], weight[i]) 
        H1pfmet_HWW_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_HWW_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_HWW_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_HWW_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_HWW_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_HWW_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif ('GluGluToZZ' in f) or ('GluGluToContinToZZ' in f):
        H1pfmet_GGZZ.Fill(pfmet[i], weight[i])
        H1pfmet_GGZZ_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_GGZZ_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])
        H1pfmet_GGZZ_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_GGZZ_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_GGZZ_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_GGZZ_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i])
        H1pfmet_GGZZ_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_GGZZ_JetResDown.Fill(pfmet_JetResDn[i], weight[i])
        H1pfmet_GGZZ_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_GGZZ_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])  
        H1pfmet_GGZZ_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_GGZZ_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_GGZZ_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_GGZZ_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif ('_ZZTo4L' in f) or ('_ZZTo2L2Nu' in f):
        H1pfmet_QQZZ.Fill(pfmet[i], weight[i])
        H1pfmet_QQZZ_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_QQZZ_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])  
        H1pfmet_QQZZ_sElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_QQZZ_sElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i]) 
        H1pfmet_QQZZ_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_QQZZ_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_QQZZ_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_QQZZ_JetResDown.Fill(pfmet_JetResDn[i], weight[i]) 
        H1pfmet_QQZZ_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_QQZZ_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i]) 
        H1pfmet_QQZZ_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_QQZZ_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_QQZZ_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_QQZZ_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif ('ZZZ' in f) or ('WZZ' in f) or ('WWZ' in f):
        H1pfmet_VVV.Fill(pfmet[i], weight[i])
        H1pfmet_VVV_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_VVV_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])   
        H1pfmet_VVV_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_VVV_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])
        H1pfmet_VVV_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_VVV_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i]) 
        H1pfmet_VVV_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_VVV_JetResDown.Fill(pfmet_JetResDn[i], weight[i])
        H1pfmet_VVV_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_VVV_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i]) 
        H1pfmet_VVV_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_VVV_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_VVV_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_VVV_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      elif ('TTW' in f) or ('TTZ' in f):
        H1pfmet_TTV.Fill(pfmet[i], weight[i])
        H1pfmet_TTV_JetEnUp.Fill(pfmet_JetEnUp[i], weight[i])
        H1pfmet_TTV_JetEnDown.Fill(pfmet_JetEnDn[i], weight[i])           
        H1pfmet_TTV_ElectronEnUp.Fill(pfmet_ElectronEnUp[i], weight[i])
        H1pfmet_TTV_ElectronEnDown.Fill(pfmet_ElectronEnDn[i], weight[i])   
        H1pfmet_TTV_MuonEnUp.Fill(pfmet_MuonEnUp[i], weight[i])
        H1pfmet_TTV_MuonEnDown.Fill(pfmet_MuonEnDn[i], weight[i])  
        H1pfmet_TTV_JetResUp.Fill(pfmet_JetResUp[i], weight[i])
        H1pfmet_TTV_JetResDown.Fill(pfmet_JetResDn[i], weight[i]) 
        H1pfmet_TTV_UnclusteredEnUp.Fill(pfmet_UnclusteredEnUp[i], weight[i])
        H1pfmet_TTV_UnclusteredEnDown.Fill(pfmet_UnclusteredEnDn[i], weight[i])
        H1pfmet_TTV_PhotonEnUp.Fill(pfmet_PhotonEnUp[i], weight[i])
        H1pfmet_TTV_PhotonEnDown.Fill(pfmet_PhotonEnDn[i], weight[i])  
        H1pfmet_TTV_FakeUp.Fill(pfmet[i], weight[i]*fake_weight)
        H1pfmet_TTV_FakeDown.Fill(pfmet[i], weight[i]*(-fake_weight))
      
        
    # Print yields  
    err2 = 0;
    for i in range(0, H1pfmet.GetXaxis().GetNbins()):
      err2 += H1pfmet.GetBinError(i)**2;

    print 'Sample name ' + args.channel + 'channel: ' + f + ' N Entries: ' + str(H1pfmet.GetEntries()) + ' Yield: ' + str(H1pfmet.Integral()) + ' Error: ' + str(math.sqrt(err2))

    # Write shape histogram to file for Monte Carlo samples
    nRebin = 1
    fs = TFile('datacards_' + args.channel + '/f' + args.channel + '.root', 'UPDATE')
    if (not fs.FindKey('bin' + args.channel)):  d = fs.mkdir('bin' + args.channel)

    if ('Run2016' in f) or ('MonoHZZ' in f) or ('Zprime' in f):
      hs = H1pfmet
      name = f.split('_25ns/')[1].split('.root')[0]
      hs.SetName(name)
      hs_rebin = hs.Rebin(nRebin, name)
      fs.cd('bin' + args.channel)
      hs_rebin.Write(name)
      
    #if 'Run2016' not in f: 
    if ('MonoHZZ' in f) or ('Zprime' in f):
      
      Integral=H1pfmet_FakeUp.Integral()
      if Integral != 0:
        H1pfmet_FakeUp.Scale(H1pfmet.Integral()/Integral)
      hs_FakeUp = H1pfmet_FakeUp
      name_FakeUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_FakeUp"
      hs_FakeUp.SetName(name_FakeUp)
      hs_FakeUp_rebin = hs_FakeUp.Rebin(nRebin, name_FakeUp)
      Integral=H1pfmet_FakeDn.Integral()
      if Integral != 0:
        H1pfmet_FakeDn.Scale(H1pfmet.Integral()/Integral)
      hs_FakeDown = H1pfmet_FakeDn
      name_FakeDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_FakeDown"
      hs_FakeDown.SetName(name_FakeDown)
      hs_FakeDown_rebin = hs_FakeDown.Rebin(nRebin, name_FakeDown)

      hs_JetEnUp = H1pfmet_JetEnUp    
      name_JetEnUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_JetEnUp"
      hs_JetEnUp.SetName(name_JetEnUp)
      hs_JetEnUp_rebin = hs_JetEnUp.Rebin(nRebin, name_JetEnUp)
      hs_JetEnDown = H1pfmet_JetEnDown    
      name_JetEnDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_JetEnDown"
      hs_JetEnDown.SetName(name_JetEnDown)
      hs_JetEnDown_rebin = hs_JetEnDown.Rebin(nRebin, name_JetEnDown)
      
      hs_ElectronEnUp = H1pfmet_ElectronEnUp    
      name_ElectronEnUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_ElectronEnUp"
      hs_ElectronEnUp.SetName(name_ElectronEnUp)
      hs_ElectronEnUp_rebin = hs_ElectronEnUp.Rebin(nRebin, name_ElectronEnUp)
      hs_ElectronEnDown = H1pfmet_ElectronEnDown    
      name_ElectronEnDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_ElectronEnDown"
      hs_ElectronEnDown.SetName(name_ElectronEnDown)
      hs_ElectronEnDown_rebin = hs_ElectronEnDown.Rebin(nRebin, name_ElectronEnDown)
      
      hs_MuonEnUp = H1pfmet_MuonEnUp    
      name_MuonEnUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_MuonEnUp"
      hs_MuonEnUp.SetName(name_MuonEnUp)
      hs_MuonEnUp_rebin = hs_MuonEnUp.Rebin(nRebin, name_MuonEnUp)
      hs_MuonEnDown = H1pfmet_MuonEnDown    
      name_MuonEnDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_MuonEnDown"
      hs_MuonEnDown.SetName(name_MuonEnDown)
      hs_MuonEnDown_rebin = hs_MuonEnDown.Rebin(nRebin, name_MuonEnDown)
      
      hs_JetResUp = H1pfmet_JetResUp    
      name_JetResUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_JetResUp"
      hs_JetResUp.SetName(name_JetResUp)
      hs_JetResUp_rebin = hs_JetResUp.Rebin(nRebin, name_JetResUp)
      hs_JetResDown = H1pfmet_JetResDown    
      name_JetResDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_JetResDown"
      hs_JetResDown.SetName(name_JetResDown)
      hs_JetResDown_rebin = hs_JetResDown.Rebin(nRebin, name_JetResDown)
      
      hs_UnclusteredEnUp = H1pfmet_UnclusteredEnUp    
      name_UnclusteredEnUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_UnclusteredEnUp"
      hs_UnclusteredEnUp.SetName(name_UnclusteredEnUp)
      hs_UnclusteredEnUp_rebin = hs_UnclusteredEnUp.Rebin(nRebin, name_UnclusteredEnUp)
      hs_UnclusteredEnDown = H1pfmet_UnclusteredEnDown    
      name_UnclusteredEnDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_UnclusteredEnDown"
      hs_UnclusteredEnDown.SetName(name_UnclusteredEnDown)
      hs_UnclusteredEnDown_rebin = hs_UnclusteredEnDown.Rebin(nRebin, name_UnclusteredEnDown)
      
      hs_PhotonEnUp = H1pfmet_PhotonEnUp    
      name_PhotonEnUp = f.split('_25ns/')[1].split('.root')[0] +  "_MET_PhotonEnUp"
      hs_PhotonEnUp.SetName(name_PhotonEnUp)
      hs_PhotonEnUp_rebin = hs_PhotonEnUp.Rebin(nRebin, name_PhotonEnUp)
      hs_PhotonEnDown = H1pfmet_PhotonEnDown    
      name_PhotonEnDown = f.split('_25ns/')[1].split('.root')[0] +  "_MET_PhotonEnDown"
      hs_PhotonEnDown.SetName(name_PhotonEnDown)
      hs_PhotonEnDown_rebin = hs_PhotonEnDown.Rebin(nRebin, name_PhotonEnDown)
      
      
      hs_JetEnUp_rebin.Write(name_JetEnUp) 
      hs_JetEnDown_rebin.Write(name_JetEnDown)       
      hs_ElectronEnUp_rebin.Write(name_ElectronEnUp) 
      hs_ElectronEnDown_rebin.Write(name_ElectronEnDown) 
      hs_MuonEnUp_rebin.Write(name_MuonEnUp) 
      hs_MuonEnDown_rebin.Write(name_MuonEnDown)   
      hs_JetResUp_rebin.Write(name_JetResUp) 
      hs_JetResDown_rebin.Write(name_JetResDown) 
      hs_UnclusteredEnUp_rebin.Write(name_UnclusteredEnUp) 
      hs_UnclusteredEnDown_rebin.Write(name_UnclusteredEnDown) 
      hs_PhotonEnUp_rebin.Write(name_PhotonEnUp) 
      hs_PhotonEnDown_rebin.Write(name_PhotonEnDown) 
      hs_FakeUp_rebin.Write(name_FakeUp)
      hs_FakeDown_rebin.Write(name_FakeDown)

    fs.Close()
   
 
  # Write data shape histogram to file
  newfs = TFile('datacards_' + args.channel + '/f' + args.channel + '.root', 'UPDATE')
  if (not newfs.FindKey('bin' + args.channel)):  d = newfs.mkdir('bin' + args.channel)
  newhs = H1pfmet_D
  newhs.SetName('data_obs')
  newhs_rebin = newhs.Rebin(nRebin, 'data_obs')
  newfs.cd('bin' + args.channel)
  newhs_rebin.Write('data_obs')

  newhs = H1pfmet_wH
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_wH_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_wH_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  wH_Integral=H1pfmet_wH_FakeUp.Integral()
  if wH_Integral != 0:
    H1pfmet_wH_FakeUp.Scale(H1pfmet_wH.Integral()/wH_Integral)
  newhs = H1pfmet_wH_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  wH_Integral=H1pfmet_wH_FakeDown.Integral()
  if wH_Integral != 0:
    H1pfmet_wH_FakeDown.Scale(H1pfmet_wH.Integral()/wH_Integral)
  newhs = H1pfmet_wH_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  
  newhs = H1pfmet_ZH
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ZH_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ZH_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ZH_Integral=H1pfmet_ZH_FakeUp.Integral()
  if ZH_Integral != 0:
    H1pfmet_ZH_FakeUp.Scale(H1pfmet_ZH.Integral()/ZH_Integral)
  newhs = H1pfmet_ZH_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ZH_Integral=H1pfmet_ZH_FakeDown.Integral()
  if ZH_Integral != 0:
    H1pfmet_ZH_FakeDown.Scale(H1pfmet_ZH.Integral()/ZH_Integral)
  newhs = H1pfmet_ZH_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  
  newhs = H1pfmet_ggH
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ggH_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ggH_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ggH_Integral=H1pfmet_ggH_FakeUp.Integral()
  if ggH_Integral != 0:
    H1pfmet_ggH_FakeUp.Scale(H1pfmet_ggH.Integral()/ggH_Integral)
  newhs = H1pfmet_ggH_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ggH_Integral=H1pfmet_ggH_FakeDown.Integral()
  if ggH_Integral != 0:
    H1pfmet_ggH_FakeDown.Scale(H1pfmet_ggH.Integral()/ggH_Integral)
  newhs = H1pfmet_ggH_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  newhs = H1pfmet_VBFH
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VBFH_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VBFH_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  VBFH_Integral=H1pfmet_VBFH_FakeUp.Integral()
  if VBFH_Integral != 0:
    H1pfmet_VBFH_FakeUp.Scale(H1pfmet_VBFH.Integral()/VBFH_Integral)
  newhs = H1pfmet_VBFH_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  VBFH_Integral=H1pfmet_VBFH_FakeDown.Integral()
  if VBFH_Integral != 0:
    H1pfmet_VBFH_FakeDown.Scale(H1pfmet_VBFH.Integral()/VBFH_Integral)
  newhs = H1pfmet_VBFH_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  
  newhs = H1pfmet_ttH
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_ttH_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_ttH_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ttH_Integral=H1pfmet_ttH_FakeUp.Integral()
  if ttH_Integral != 0:
    H1pfmet_ttH_FakeUp.Scale(H1pfmet_ttH.Integral()/ttH_Integral)
  newhs = H1pfmet_ttH_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  ttH_Integral=H1pfmet_ttH_FakeDown.Integral()
  if ttH_Integral != 0:
    H1pfmet_ttH_FakeDown.Scale(H1pfmet_ttH.Integral()/ttH_Integral)
  newhs = H1pfmet_ttH_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  
  newhs = H1pfmet_HWW
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_HWW_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_HWW_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  HWW_Integral=H1pfmet_HWW_FakeUp.Integral()
  if HWW_Integral != 0:
    H1pfmet_HWW_FakeUp.Scale(H1pfmet_HWW.Integral()/HWW_Integral)
  newhs = H1pfmet_HWW_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  HWW_Integral=H1pfmet_HWW_FakeDown.Integral()
  if HWW_Integral != 0:
    H1pfmet_HWW_FakeDown.Scale(H1pfmet_HWW.Integral()/HWW_Integral)
  newhs = H1pfmet_HWW_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  newhs = H1pfmet_GGZZ
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_GGZZ_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_GGZZ_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  GGZZ_Integral=H1pfmet_GGZZ_FakeUp.Integral()
  if GGZZ_Integral != 0:
    H1pfmet_GGZZ_FakeUp.Scale(H1pfmet_GGZZ.Integral()/GGZZ_Integral)
  newhs = H1pfmet_GGZZ_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  GGZZ_Integral=H1pfmet_GGZZ_FakeDown.Integral()
  if GGZZ_Integral != 0:
    H1pfmet_GGZZ_FakeDown.Scale(H1pfmet_GGZZ.Integral()/GGZZ_Integral)
  newhs = H1pfmet_GGZZ_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  newhs = H1pfmet_QQZZ
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_sElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_sElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_QQZZ_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_QQZZ_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  QQZZ_Integral=H1pfmet_QQZZ_FakeUp.Integral()
  if QQZZ_Integral != 0:
    H1pfmet_QQZZ_FakeUp.Scale(H1pfmet_QQZZ.Integral()/QQZZ_Integral)
  newhs = H1pfmet_QQZZ_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  QQZZ_Integral=H1pfmet_QQZZ_FakeDown.Integral()
  if QQZZ_Integral != 0:
    H1pfmet_QQZZ_FakeDown.Scale(H1pfmet_QQZZ.Integral()/QQZZ_Integral)
  newhs = H1pfmet_QQZZ_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  
  newhs = H1pfmet_VVV
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_VVV_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_VVV_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  VVV_Integral=H1pfmet_VVV_FakeUp.Integral()
  if VVV_Integral != 0:
    H1pfmet_VVV_FakeUp.Scale(H1pfmet_VVV.Integral()/VVV_Integral)
  newhs = H1pfmet_VVV_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  VVV_Integral=H1pfmet_VVV_FakeDown.Integral()
  if VVV_Integral != 0:
    H1pfmet_VVV_FakeDown.Scale(H1pfmet_VVV.Integral()/VVV_Integral)
  newhs = H1pfmet_VVV_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()

  newhs = H1pfmet_TTV
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_JetEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_JetEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_ElectronEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_ElectronEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_MuonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_MuonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_JetResUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_JetResDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_UnclusteredEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_UnclusteredEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  newhs = H1pfmet_TTV_PhotonEnUp
  newfs.cd('bin' + args.channel)
  newhs.Write()    
  newhs = H1pfmet_TTV_PhotonEnDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  TTV_Integral=H1pfmet_TTV_FakeUp.Integral()
  if TTV_Integral != 0:
    H1pfmet_TTV_FakeUp.Scale(H1pfmet_TTV.Integral()/TTV_Integral)
  newhs = H1pfmet_TTV_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.Write()
  TTV_Integral=H1pfmet_TTV_FakeDown.Integral()
  if TTV_Integral != 0:
    H1pfmet_TTV_FakeDown.Scale(H1pfmet_TTV.Integral()/TTV_Integral)
  newhs = H1pfmet_TTV_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.Write()
  
  newhs = H1pfmet_ZX
  newfs.cd('bin' + args.channel)
  newhs.SetName("ZX")
  newhs.Write("ZX",TObject.kWriteDelete)

 
#  newhs = H1pfmet_ZX_JetEnUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_JetEnUp")
#  newhs.Write("ZX_MET_JetEnUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_JetEnDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_JetEnDown")
#  newhs.Write("ZX_MET_JetEnDown",TObject.kWriteDelete)
  
#  newhs = H1pfmet_ZX_MET_ElectronEnUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_ElectronEnUp")
#  newhs.Write("ZX_MET_ElectronEnUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_ElectronEnDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_ElectronEnDown")
#  newhs.Write("ZX_MET_ElectronEnDown",TObject.kWriteDelete)
  
#  newhs = H1pfmet_ZX_MuonEnUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_MuonEnUp")
#  newhs.Write("ZX_MET_MuonEnUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_MET_MuonEnDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_MuonEnDown")
#  newhs.Write("ZX_MET_MuonEnDown",TObject.kWriteDelete)
  
#  newhs = H1pfmet_ZX_JetResUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_JetResUp")
#  newhs.Write("ZX_MET_JetResUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_JetResDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_JetResDown")
#  newhs.Write("ZX_MET_JetResDown",TObject.kWriteDelete)
  
#  newhs = H1pfmet_ZX_UnclusteredEnUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_UnclusteredEnUp")
#  newhs.Write("ZX_MET_UnclusteredEnUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_UnclusteredEnDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_UnclusteredEnDown")
#  newhs.Write("ZX_UnclusteredEnDown",TObject.kWriteDelete)

#  newhs = H1pfmet_ZX_PhotonEnUp
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_PhotonEnUp")
#  newhs.Write("ZX_MET_PhotonEnUp",TObject.kWriteDelete)
#  newhs = H1pfmet_ZX_PhotonEnDown
#  newfs.cd('bin' + args.channel)
#  newhs.SetName("ZX_MET_PhotonEnDown")
#  newhs.Write("ZX_MET_PhotonEnDown",TObject.kWriteDelete)


  newhs = H1pfmet_ZX_FakeUp
  newfs.cd('bin' + args.channel)
  newhs.SetName("ZX_MET_FakeUp")
  newhs.Write("ZX_MET_FakeUp",TObject.kWriteDelete)
  newhs = H1pfmet_ZX_FakeDown
  newfs.cd('bin' + args.channel)
  newhs.SetName("ZX_MET_FakeDown")
  newhs.Write("ZX_MET_FakeDown",TObject.kWriteDelete)


newfs.Close()
   
