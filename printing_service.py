# printing_service.py

import pdf2final_list
import text2ppt
import gui

# Process topics and generate the presentation
x = pdf2final_list.process(["Logistic Regression", "Estimating Probabilities in ML",
                            "Training and cost function in ML", "Decision boundaries in ML",
                            "SoftMax regression", "Non-linear SVM classification",
                            "Polynomial kernel in SVM", "Adding similarity feature in SVM",
                            "Gaussian RBF Kernel in SVM", "SVM Regression"])
text2ppt.presentate(x)
