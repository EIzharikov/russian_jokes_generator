"""
Module of dataset preparation for further model fine-tuning on scraped russian jokes
"""
import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv("spider/anecdotes_dataset.csv")
    data.drop(columns=["Unnamed: 0"], inplace=True)

    result_ds = pd.DataFrame(
        {
            "prompt": [
                f"<|startoftext{tag}|>{text}"
                for tag, text in zip(data["tag"].values, data["text"].values)
            ]
        }
    )

    # splitting data into training and validation sets
    training_data = result_ds.sample(frac=0.8, random_state=25)
    validation_data = result_ds.drop(training_data.index)

    # writing sets to txt files
    training_data.to_csv(
        "models/models_config/custom/train.txt",
        sep="\n",
        header=False,
        index=False,
        mode="a",
    )
    validation_data.to_csv(
        "models/models_config/custom/valid.txt",
        sep="\n",
        header=False,
        index=False,
        mode="a",
    )
