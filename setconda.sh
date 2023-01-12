set -xv
export CONDAPATH="/goinfre/$USER/miniconda3"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
sh Miniconda3-latest-Linux-x86_64.sh -b -p $CONDAPATH
$CONDAPATH/bin/conda init zsh
$CONDAPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
rm Miniconda3-latest-Linux-x86_64.sh