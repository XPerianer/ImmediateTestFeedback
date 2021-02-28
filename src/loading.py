#
# The MIT License (MIT)
#
# Copyright (c) 2020-2021 Dominik Meier
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
import pandas as pd


def load_dataset(filename, sparsify=False):
    mutants_and_tests = pd.read_pickle(filename)
    mutants_and_tests.reset_index()
    mutants_and_tests["outcome"] = mutants_and_tests["outcome"].astype("bool")
    mutants_and_tests["outcome"]
    if sparsify:
        keep_fraction = 0.05  # Keep 5% of the dataset (roughly, since we delete tests and mutants smaller than that)
        max_mutant_id = mutants_and_tests["mutant_id"].max()
        max_test_id = max(
            mutants_and_tests["test_id"].max(), 10
        )  # At least use 10 tests
        return mutants_and_tests.loc[
            mutants_and_tests["test_id"] < max_test_id * keep_fraction
        ].loc[mutants_and_tests["mutant_id"] < max_mutant_id * keep_fraction]
    return mutants_and_tests


def load_datasets(name_and_filename, sparsify=False):
    datasets = {}
    for name, filename in name_and_filename.items():
        datasets[name] = load_dataset(filename, sparsify)
    return datasets
