from clearml import PipelineDecorator, PipelineController, Task
from _1_basic import PROJECT_NAME


QUEUE_NAME = "gizatulin_queue"

def make_pipe():
    pipe = PipelineController(
        name="Pipeline demo",
        project=PROJECT_NAME,
        version="0.0.1",
        add_pipeline_tags=False,
    )
    pipe.set_default_execution_queue(QUEUE_NAME)
    pipe.add_step()

if __name__ == '__main__':
    # run the pipeline on the current machine, for local debugging
    # for scale-out, comment-out the following line (Make sure a
    # 'services' queue is available and serviced by a ClearML agent
    # running either in services mode or through K8S/Autoscaler)
    PipelineDecorator.run_locally()
    pipeline_logic(do_stuff=True)
