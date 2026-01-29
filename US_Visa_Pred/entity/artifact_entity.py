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
    