cd ../../

currpath=`pwd`
# train the model
python matchzoo/main.py --phase train --model_file ${currpath}/examples/InsuranceQA/config/arci_insuranceqa.config


# predict with the model
python matchzoo/main.py --phase predict --model_file ${currpath}/examples/InsuranceQA/config/arci_insuranceqa.config
