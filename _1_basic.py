import random
from pathlib import Path

from clearml import Task, Model, InputModel, OutputModel, Dataset, Logger
import pandas as pd
import matplotlib.pyplot as plt


PROJECT_NAME = "gizatulin_test_project/demo_prep"


def main():
    # Task create
    task = Task.init(project_name=PROJECT_NAME, task_name='basic_1', task_type=Task.TaskTypes.testing)

    # Set HyperParams
    task.set_parameters({'param_1': 'value_1', 'param_2': 'value_2'})

    # Set user properties
    task.set_user_properties(
        {
            'name': 'user_properties_1',
            'description': 'user prop_1',
            'value': 'value_1',
        },
        {
            'name': 'user_properties_2',
            'description': 'user prop_2',
            'value': 'value_2',
        },
    )

    # Some func + logging
    for i in range(10):
        task.log.debug({"train_loss": i, "valid_loss": 0.8})

    task.logger.report_media(
        title="Example media upload",
        series='some_series_example',
        local_path='./media_artifact.png',
    )

    # Registering custom artifact
    df = pd.DataFrame({'a': [0, 9, 8], 'b': [5, 6, 7]})
    task.register_artifact('train data', df)

    # Upload output model
    # Download locally from here https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5x6.pt
    file_path = Path('./yolov5x6.pt')
    if file_path.exists():
        output_model = OutputModel(task=task, config_text="Some config as text")
        # Choose where to upload (by default uploads only local address), can also be set in Logger settings
        output_model.set_upload_destination("http://clearml-fileserver.exploration.svc.k8s.datascience-dev-dp:8081")
        output_model.update_labels({"some_label": 0, "other_label": 1})
        output_model.update_weights(weights_filename='./yolov5x6.pt', auto_delete_file=False)

    # Random plot
    a = lambda : random.randint(0, 10)
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.plot([a() for _ in range(4)], [a() for _ in range(4)])  # Plot some data on the Axes.
    plt.show()  # Show the figure.

    # Scalars
    # report two scalar series on the same graph
    for i in range(100):
        Logger.current_logger().report_scalar(
            "unified graph", "series A", iteration=i, value=1. / (i + 1)
        )
        Logger.current_logger().report_scalar(
            "unified graph", "series B", iteration=i, value=10. / (i + 1)
        )

    # report two scalar series on two different graphs
    for i in range(100):
        Logger.current_logger().report_scalar(
            "graph A", "series A", iteration=i, value=1. / (i + 1)
        )
        Logger.current_logger().report_scalar(
            "graph B", "series B", iteration=i, value=10. / (i + 1)
        )


if __name__ == '__main__':
    print(main())
    # print(get_tasks())
