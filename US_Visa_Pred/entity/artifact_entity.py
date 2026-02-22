from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifact:
    validation_status: bool
    message: str
    drift_report_file_path: str
    drift_dashboard_file_path: str

@dataclass
class DataTransformationArtifact:
    preprocessor_object_file_path:str
    trained_array_file_path:str
    test_array_file_path:str

@dataclass
class ClassificatiomMetricArtifact:
    accuracy_score:float
    precision_score:float
    recall_score:float
    f1_score:float

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    metric_artifact: ClassificatiomMetricArtifact


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted:bool
    changed_accuracy:float
    s3_model_path:str 
    trained_model_path:str



@dataclass
class ModelPusherArtifact:
    bucket_name:str
    s3_model_path:str
    

    