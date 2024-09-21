impot utils

class LLM:
    def __init__(this):
        this.checkpoint = None

    def train(this, input_csv):
        # First we need to determine whether the input_csv has labeled rows and columns
        # because we will need to transform the data into a time-series like format where
        # each column would as-if correspond to a different document.

        df = pd.read_csv(input_csv)
        if utils.df_has_labeled_rows_and_columns(df)
            # Transform the data
            pass

    def predict(this, input_csv):
        pass

    def set_checkpoint(checkpoint):
        this.checkpoint = checkpoint

    def load_checkpoint():
        pass

    def save_checkpoint():
        pass