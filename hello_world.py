# Databricks notebook source
from scripts.argparse import create_parser
print("hello world")
param_value = dbutils.widgets.get("python_params")
print(param_value)