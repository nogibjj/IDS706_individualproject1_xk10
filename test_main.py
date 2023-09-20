"""
Test goes here

"""
import main
from main import summary_desc
import pandas as pd


def test_summary_desc():
    result = summary_desc()

    # test the result of main
    assert result.loc["mean", "Age"] == 31.61808367071525

    # test the result of median
    assert result.loc["50%", "Weight"] == 72.9

    # test the result of std
    assert round(result.loc["std", "Height"], 6) == 0.085974


def test_histogram():
    df = pd.read_csv("bmi.csv")

    main.histogram(df)

    # assert os.path.isfile(histogram_image_path)


if __name__ == "__main__":
    test_summary_desc()
    test_histogram()
