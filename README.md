# Used keras-frcnn
Keras implementation of Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks.
cloned from https://github.com/yhenon/keras-frcnn/

India has 1.3 billion population with a  very low doctor-patient ratio, thus most people lack access to quality healthcare. According to health reports, mortality rate of India increased from 26.83 deaths per 100 population in 1970 to 31.02 deaths per 100 population in 2015 growing at an average annual rate of 1.72 %. We don't have any system of assuring quality check on surgeons surgical skills during surgery, thus patients have to suffer many times because of the lack of surgical skills of the doctor. Improving surgical training, assuring regular feedbacks and setting up some type of norms for surgery can help us to reduce the rate of complications. To do this, it is essential to assess operative skill, a process that currently requires experts and is manual, time-consuming as many surgeries lasting hours. Real-time automated surgical video analysis could provide a way to objectively and efficiently assess surgical skills. Here, we will develop an approach to detect surgical tools in surgical videos as well as assess surgeons performance using Convolutional Neural Network. We will be using the m2cai16-tool dataset with spatial bounds of tools for training our model. The m2cai16-tool dataset with spatial bounds of tools has 7 most frequently used tools in Laparoscopic surgeries. We will not only detect presence but also spatially localize surgical tools in real-world laparoscopic surgical videos. Because of using deep learning approach which not only allows for tool localization along with frame-level detection but also enables a richer analysis of tool movements which will further help in assessing surgical quality through analysis of tool usage patterns, movement range, and economy of motion.

In 2016, M2CAI launched a challenge “surgical tool presence detection” which grabbed the attention of a lot of researchers in this field. There were several participants in this challenge, they tried various methods to achieve better and better precision. For the analysis of operative skills of surgeons, we require not just detection of the surgical tool but localized detection of the surgical tool so that we can analyse the movement of each tool during the surgery and can generate feedback for the doctors. This rich analysis using deep learning can as a guide after surgery and can also help in reducing the number of casualties during the surgery which only happens because of mishandling of surgical tools by doctors. In future, these type of rich analysis can help in generating real-time feedback during surgery which can further help doctors during complex surgeries. This richer analysis can also be used by robots as a training guide for automated complex surgeries. We have used one of these techniques of object detection for surgical tool detection and operational skill assessment of surgeons using deep learning.

Example output:

![ex1](https://i.imgur.com/DY8Yyzh.png)
![ex2](https://i.imgur.com/i41RsQh.png)
![ex3](https://i.imgur.com/xV0Xi3E.png)
![ex4](https://i.imgur.com/9eGnjoM.png)

ISSUES:

- If you get this error:
`ValueError: There is a negative shape in the graph!`    
    than update keras to the newest version

- If you run out of memory, try reducing the number of ROIs that are processed simultaneously. Try passing a lower `-n` to `train_frcnn.py`. Alternatively, try reducing the image size from the default value of 600 (this setting is found in `config.py`.
