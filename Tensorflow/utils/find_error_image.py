from per_image_evaluation import PerImageEvaluation
import numpy as np


def find_error_image(detected_boxes, detected_scores, detected_class_labels,
      groundtruth_boxes, groundtruth_class_labels, nums_classes):
    perImageEvaluation = PerImageEvaluation(nums_classes)

    groundtruth_is_difficult_list = np.array([], dtype=bool)
    groundtruth_is_group_of_list = np.array([], dtype=bool)

    scores, tp_fp_labels, is_class_correctly_detected_in_image = perImageEvaluation.compute_object_detection_metrics(
        detected_boxes, detected_scores, detected_class_labels,
        groundtruth_boxes, groundtruth_class_labels,
        groundtruth_is_difficult_list, groundtruth_is_group_of_list)
    
    

