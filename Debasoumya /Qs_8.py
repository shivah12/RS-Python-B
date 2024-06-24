{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOZQPnB33AWzSGL+FNDlCvy",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya%20/Qs_8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LdGet49kBW6u",
        "outputId": "9b0c1d82-815b-4683-d5ed-727460bc70b1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{1: 2, 5: 2, 4: 2, 3: 3, 2: 1}\n"
          ]
        }
      ],
      "source": [
        "def count(l):\n",
        "  f={}\n",
        "  for i in l:\n",
        "    if i in f:\n",
        "      f[i]+=1\n",
        "    else:\n",
        "      f[i]=1\n",
        "  print (f)\n",
        "l=[1,5,4,3,4,5,2,1,3,3]\n",
        "count(l)\n"
      ]
    }
  ]
}