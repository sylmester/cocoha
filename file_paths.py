from pathlib import Path
import re

# Define download URLs
AUDIO_URL = 'https://zenodo.org/record/1199011/files/AUDIO.zip'
DATA_PREPROC_URL = 'https://zenodo.org/record/1199011/files/DATA_preproc.zip'

# Root data directory
DATA_ROOT = Path("~").expanduser() / 'Data' / 'cocoha'

# Preprocessed data directory
DATA_PREPROC = DATA_ROOT / "data_preprocessed"

# List of subjects based on the preprocessed data files
SUBJECTS = [path.name for path in DATA_PREPROC.iterdir() if re.match(r'S\d+_data_preproc.mat', path.name)]

# Stimuli directory and list of stimulus names (without file extensions)
STIMULUS_DIR = DATA_ROOT / 'stimuli'
STIMULI_PATHS = [stimulus.stem for stimulus in STIMULUS_DIR.glob("*.wav")]

# Envelopes directory
ENVELOPES_DIR = DATA_ROOT / "envelopes"

# Predictors directory
PREDICTOR_DIR = DATA_ROOT / 'predictors'

# EEG data directory and list of subjects
EEG_DIR = DATA_ROOT / 'eeg'

# Define a target directory for TRF estimates and make sure the directory is created
TRF_DIR = DATA_ROOT / 'TRFs'


# Figures directory
FIGURES_DIR = DATA_ROOT / 'figures'

# Make sure all directories exist
for directory in [DATA_PREPROC, ENVELOPES_DIR, PREDICTOR_DIR, EEG_DIR, TRF_DIR]:
    directory.mkdir(parents=True, exist_ok=True)
