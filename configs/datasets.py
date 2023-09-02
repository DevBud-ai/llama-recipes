# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from dataclasses import dataclass

    
@dataclass
class samsum_dataset:
    dataset: str =  "samsum_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    input_length: int = 2048
    
    
@dataclass
class grammar_dataset:
    dataset: str = "grammar_dataset"
    train_split: str = "ft_datasets/grammar_dataset/gtrain_10k.csv" 
    test_split: str = "ft_datasets/grammar_dataset/grammar_validation.csv"
    input_length: int = 2048

    
@dataclass
class alpaca_dataset:
    dataset: str = "alpaca_dataset"
    train_split: str = "train"
    test_split: str = "val"
    data_path: str = "ft_datasets/dummy-instruction.json"

@dataclass
class identity_dataset:
    dataset: str = "identity_dataset"
    train_split: str = "train"
    test_split: str = "val"
    data_path: str = "ft_datasets/dummy-data-conversation.json"

@dataclass
class evol_code_dataset:
    dataset: str = "evol_code_dataset"
    train_split: str = "train"
    test_split: str = "val"
    data_path: str = "nickrosh/Evol-Instruct-Code-80k-v1"

@dataclass
class orca_dataset:
    dataset: str = "orca_dataset"
    train_split: str = "train"
    test_split: str = "val"
    data_path: str = "iamplus/Open_Platypus_Orca"