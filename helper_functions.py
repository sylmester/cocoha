import file_paths


# Utility function to get subject list
def get_subjects():
    return [path.stem.split("_")[0] for path in file_paths.DATA_PREPROC.glob("*.mat")]
