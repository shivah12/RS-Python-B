{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNV0bD4Jo5oy6xtab9jrjX4",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OYm2R7wnm1-K"
      },
      "outputs": [],
      "source": [
        "import cv2\n",
        "img=cv2.imread(\"image.jpeg\")\n",
        "l_threshold=100\n",
        "u_threshold=200\n",
        "a_size=5\n",
        "e=cv2.Canny(img,l_threshold,u_threshold,a_size)\n",
        "cv2.imshow('original',img)\n",
        "cv2.imshow('edge',edge)\n",
        "cv2.waitKey(0)\n",
        "cv2.destroyAllWindows()"
      ]
    }
  ]
}