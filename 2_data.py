# Docs - https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/

# clearml-data create --project="gizatulin_test_project/demo_prep" --name="example_dataset" --version=0.0.1 --storage="http://clearml-fileserver.exploration.svc.k8s.datascience-dev-dp:8081"
# clearml-data add --id=635f047c7d3543be8b22d2fea36d358f --files=./f1
# clearml-data upload --id=635f047c7d3543be8b22d2fea36d358f
# clearml-data sync --id=635f047c7d3543be8b22d2fea36d358f


# clearml-data close --id=bd97165436754714a82dce117380d0fe --verbose

# Python way
from clearml import Dataset
from _1_basic import PROJECT_NAME

dataset_name = "example_dataset"
dataset_project = PROJECT_NAME

dataset_path = Dataset.get(
    dataset_id="635f047c7d3543be8b22d2fea36d358f",
    # dataset_name=dataset_name,
    # dataset_project=dataset_project,
).get_local_copy()

