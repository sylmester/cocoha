import file_paths
import re


# Utility function to get subject list
def get_subjects():
    SUBJECTS = [path.stem.split("_")[0] for path in file_paths.DATA_PREPROC.glob("*.mat")]
    SUBJECTS = sorted(SUBJECTS, key=lambda x: int(re.search(r'S(\d+)', x).group(1)))
    return SUBJECTS

# Utility function to get stimulus paths
def get_stimuli_paths():
    return [stimulus.stem for stimulus in file_paths.STIMULUS_DIR.glob("*.wav")]

# Get subject data file path
def get_subject_data_file(subject: str):
    return file_paths.DATA_PREPROC / f"{subject}_data_preproc.mat"
