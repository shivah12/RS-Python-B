{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOgQ2aznt53v9juAz0/i4fl",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Debasoumya\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "JyWeJHoyktWG"
      },
      "outputs": [],
      "source": [
        "s=input('Enter 1st string')\n",
        "t=input('Enter 2nd string')\n",
        "s=s.lower()\n",
        "t=t.lower()\n",
        "if(len(s)==len(t)):\n",
        "  if(sorted(t)==sorted(s)):\n",
        "    print('TRUE')\n",
        "  else:\n",
        "    print('FALSE')\n",
        "else:\n",
        "    print(\"tands are not anagram\")"
      ]
    }
  ]
}
