## 0.1.0 (一月 24, 2020)
  - initialization: added bump-version.sh and modified .gitignore
  - Merge pull request #156 from EverWinter23/patch-2
  - datasets.py: Convert image to RGB channel
  - Update README.md
  - Merge pull request #152 from timforby/patch-1
  - Preserve filenames of images produced by detect.py
  - allow for unscaled/non-normalized labels
  - Update README.md
  - Update README.md
  - Clean up
  - Common download weights script
  - Clean up
  - Update README.md
  - Update README.md
  - Merge pull request #151 from eriklindernoren/custom-training
  - README
  - README
  - README
  - Add support for loading backend weights pretrained on COCO
  - Docs
  - Merge branch 'custom-training' of https://github.com/eriklindernoren/PyTorch-YOLOv2 into custom-training
  - Docs
  - Merge branch 'master' into custom-training
  - Changed parameter names
  - Update README.md
  - Merge pull request #150 from timforby/master
  - Doc
  - Clean up
  - Removed custom model def.
  - Merge
  - Model evaluation after each epoch. Training on custom dataset instructions
  - Update README.md
  - Fix example label
  - Instructions for training on custom dataset
  - Fix error with compute_map, targets were expecting batch dimension but collate_fn reduces that dimension. Removed that slicing index and now works.
  - Clean up
  - Typo fix
  - Fix resize
  - Evaluates model on validation set after each epoch
  - Clean up
  - Multiscale : New size every tenth batch
  - More efficient multiscale training. Pillow instead of lycon
  - Added license
  - Merge branch 'master' of https://github.com/eriklindernoren/PyTorch-YOLOv
  - Added method for rescaling bounding boxes to original image
  - Update README.md
  - Update README.md
  - Update README.md
  - Fix Darknet.save_weights
  - Old var names
  - README
  - Clean up
  - Fixed test.py
  - Fix test.py and remove bbox iou compute for numpy arrays
  - Fixes bug in models.create_modules (shortcut and route layers)
  - Added if __name__ == '__main__'
  - Handles batch with no targets
  - Removed dev print
  - Removed use of Pillow. Updated requirements
  - Update README.md
  - Update README.md
  - Update README.md
  - Update README.md
  - Significantly faster training
  - Set loss parameters to balance precision / recall during training
  - Revert to pad 127.5
  - Faster. Resolves #139.
  - Logs recall50 and recall75. More efficient Tensorboard logging.
  - Fix Tensorboard logging
  - Update README.md
  - Update README.md
  - Update README.md
  - Changed log format
  - terminaltables for nicer logging
  - Multi-scale training
  - Merge branch 'master' of https://github.com/eriklindernoren/PyTorch-YOLOv3
  - Multi-scale training
  - Update README.md
  - Adds option to compute and log mAP during training
  - Removed CE
  - Use BCE as class loss (as in paper)
  - Gradient accumulation before step + clean up
  - Classification logging
  - Log approximate time left for epoch
  - Log expected time left for epoch
  - Clean up
  - Log losses (in Tensorboard and stdout) at each YOLO layer
  - Tensorboard
  - Merge pull request #137 from timforby/master
  - fix incorrect class loss calculation. cross entropy being averaged twice due to PyTorch defaults
  - Update README.md
  - Added score threshold when computing predictions for recall / precision
  - Added precision to train log
  - Balancing between obj and noobj part of confidence loss. Computation of mAP by class-wise average of APs.
  - Balancing between obj and noobj part of confidence loss. Computation of mAP by class-wise average of APs.
  - Balancing between obj and noobj part of confidence loss. Computation of mAP by class-wise average of APs.
  - Merge pull request #48 from id9502/master
  - Now tiny yolo-v3 can be used as detecting network, which is lightweight and can run about 5x faster than full Yolo-v3
  - Confidence mask according to paper using ignore threshold
  - Confidence mask according to paper using ignore threshold
  - Fix training bug when annotations are missing. Changed AP to recall
  - Added argument use_cuda
  - Computation of mAP
  - Merge branch 'master' of https://github.com/eriklindernoren/PyTorch-YOLO-V3
  - Fix to utils.bbox_iou. Stabilizes training. Resolves #25 #23 #18 #13 #12
  - Update README.md
  - Merge pull request #15 from 0asa/patch-1
  - Image folder argument was not used
  - Log progress in train.py
  - Bug fix in YOLOLayer.forward
  - Bug fix in YOLOLayer.forward
  - Merge pull request #8 from catalinolaru1/master
  - Added save_weights
  - Update README.md
  - Update README.md
  - Merge branch 'master' of https://github.com/eriklindernoren/PyTorch-YOLO-V3
  - torch.no_grad() in detect.py and test.py
  - Update README.md
  - Reproduced author's performance on COCO test
  - Update README.md
  - Update README.md
  - Update README.md
  - Merge
  - Reproduced author's performance on COCO test
  - Update README.md
  - Update README.md
  - Training refinements. Mostly work in YOLOLayer.forward and utils.build_targets
  - Training support! : )
  - Deleted root datasets.py. Updated installation instructions.
  - Support for loading coco. Preparation for training support
  - Simplified non-maximum suppression and faster test script.
  - Merge branch 'master' of https://github.com/eriklindernoren/PyTorch-YOLO-V3
  - CUDA support fix for non_max_suppression. Resolves #1
  - Update README.md
  - Update README.md
  - Update README.md
  - Removed output folder and replaced it with assets folder, which contains samples for README
  - Clean up
  - Added sample to README
  - Changed default confidence threshold for inference script
  - Cleaned up non-maximum suppression. Added arguments
  - Clean up
  - Created YOLO layer. Prep for training support
  - Update README.md
  - Update README.md
  - Update README.md
  - Update README.md
  - Update README.md
  - Refined image outputs
  - Initial commit
  - Initial commit

