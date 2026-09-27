"""Fail CI if any DAG in dags/ cannot be loaded by Airflow."""

import sys

try:
    from airflow.dag_processing.dagbag import DagBag
except ImportError:
    from airflow.models.dagbag import DagBag

dagbag = DagBag(dag_folder="/opt/airflow/dags", include_examples=False)

if dagbag.import_errors:
    for path, error in dagbag.import_errors.items():
        print(f"Import error in {path}:\n{error}")
    sys.exit(1)

if not dagbag.dags:
    print("No DAGs found in dags/")
    sys.exit(1)

print("DAGs loaded OK:", ", ".join(sorted(dagbag.dag_ids)))
