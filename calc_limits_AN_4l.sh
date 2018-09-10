#!/bin/bash
# -----------------------------------------------------------------------------
#  File:        calc_limits_AN_4l.sh
#  Usage:       bash calc_limits_AN_4l.sh 4l
#  Description: Runs the sequence of steps to calculate and plot cross section
#               upper limits using event yields from the HiggsAnalysis/HiggsToZZ4Leptons
#               selection framework.
#  Created:     Nicola De Filippis
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
#   Loop through input files, printing out yields and outputting root files containing
#   shape distributions.
# -----------------------------------------------------------------------------


  # Zp2HDM
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8.txt datacards_4e/hhxx_Spring16_card_4e_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8.txt > datacards_4l/hhxx_Spring16_card_4l_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8.txt

  # ZpBaryonic
  # combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph.txt
  combineCards.py datacards_4mu/hhxx_Spring16_card_4mu_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph.txt datacards_4e/hhxx_Spring16_card_4e_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph.txt datacards_2e2mu/hhxx_Spring16_card_2e2mu_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph.txt > datacards_4l/hhxx_Spring16_card_4l_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph.txt

  sed -i -e 's/datacards_4mu\/datacards_4mu\//datacards_4mu\//g' datacards_4l/hhxx_Spring16_card_4l_*.txt
  sed -i -e 's/datacards_4e\/datacards_4e\//datacards_4e\//g' datacards_4l/hhxx_Spring16_card_4l_*.txt
  sed -i -e 's/datacards_2e2mu\/datacards_2e2mu\//datacards_2e2mu\//g' datacards_4l/hhxx_Spring16_card_4l_*.txt

  #sed -i -e 's/datacards/ZZ\/datacards/g' datacards_4l/hhxx_Fall15_card_4l_*.txt



# -----------------------------------------------------------------------------
#  Run the Asymptotic method of the combine tool on the data cards, outputting limits to 
#  txt files.
# -----------------------------------------------------------------------------
echo '-----------------------------------------------------------------------------'
echo 'Step 4: Calculate limits for different signals'
echo '-----------------------------------------------------------------------------'

# Zp2HDM
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1000_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP1000_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1200_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP1200_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1400_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP1400_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-1700_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP1700_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2000_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP2000_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-2500_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP2500_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-600_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP600_MA0300.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8.txt -n _$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-800_MA0-300_13TeV-madgraph-pythia8 -m 125 > limits_$1_MZP800_MA0300.txt

mv -f higgsCombine_$1_ZprimeToA0hToA0chichihZZTo4l_2HDM_MZp-*_MA0-300_13TeV-madgraph*.AsymptoticLimits.mH125.root datacards_$1/.

# ZpBaryonic
# combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP10000_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP1000_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP100_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP10_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP2000_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP200_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP20_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP300_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP500_MChi1.txt
combine -M AsymptoticLimits datacards_$1/hhxx_Spring16_card_$1_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph.txt -n _$1_MonoHZZ4l_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph -m 125 > limits_$1_ZpBaryonic_MZP50_MChi1.txt

mv -f higgsCombine_$1_MonoHZZ4l_ZpBaryonic_MZp-*_MChi-1_13TeV-madgraph.AsymptoticLimits.mH125.root  datacards_$1/.

# -----------------------------------------------------------------------------
#  Combine txt files containing limits in order for plotting.
# -----------------------------------------------------------------------------
echo '-----------------------------------------------------------------------------'
echo 'Step 5: Merge txt files in ascending MZP order'
echo '-----------------------------------------------------------------------------'
cat limits_$1_MZP600_MA0300.txt limits_$1_MZP800_MA0300.txt limits_$1_MZP1000_MA0300.txt limits_$1_MZP1200_MA0300.txt limits_$1_MZP1400_MA0300.txt limits_$1_MZP1700_MA0300.txt limits_$1_MZP2000_MA0300.txt limits_$1_MZP2500_MA0300.txt > limits_Zp2HDM_$1_MA0300.txt

cat limits_$1_ZpBaryonic_MZP10_MChi1.txt limits_$1_ZpBaryonic_MZP20_MChi1.txt limits_$1_ZpBaryonic_MZP50_MChi1.txt limits_$1_ZpBaryonic_MZP100_MChi1.txt limits_$1_ZpBaryonic_MZP200_MChi1.txt limits_$1_ZpBaryonic_MZP300_MChi1.txt limits_$1_ZpBaryonic_MZP500_MChi1.txt limits_$1_ZpBaryonic_MZP1000_MChi1.txt limits_$1_ZpBaryonic_MZP2000_MChi1.txt limits_$1_ZpBaryonic_MZP10000_MChi1.txt > limits_ZpBaryonic_$1_MChi1.txt


# -----------------------------------------------------------------------------
#  Parse the limits file for median and +/- 1,2 sigma limits numbers only for plotting.
# -----------------------------------------------------------------------------
echo '-----------------------------------------------------------------------------'
echo 'Step 6: Parse merged txt file to extract limits'
echo '-----------------------------------------------------------------------------'
#python format_limits.py $1 Zp2HDM
#python format_limits.py $1 ZpBaryonic


# -----------------------------------------------------------------------------
#  Parse the output of Step 6 and create limit plots, properly scaled.
# -----------------------------------------------------------------------------
echo '-----------------------------------------------------------------------------'
echo 'Step 7: Plot limits'
echo '-----------------------------------------------------------------------------'
#mkdir -p plots
#root -b -q -l "limitPlots_Zp2HDM.C(\"$1\")"
#root -b -q -l "limitPlots_ZpBaryonic.C(\"$1\")"
