{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN5+EHqNjI0k0J0apDRmzUw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KhhbaFhwlCMc"
      },
      "outputs": [],
      "source": [
        "import cv2\n",
        "v=cv2.VideoCapture(0)\n",
        "while (True):\n",
        "    isTrue,frame=capture.read()\n",
        "    cv2.imshow(\"frame\",frame)\n",
        "    if cv2.waitKey(1) & 0xFF==ord('b'):\n",
        "        break\n",
        "v.release()\n",
        "cv2.destroyAllWindows()"
      ]
    }
  ]
}