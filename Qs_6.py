{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOeluzEd+yc3uDrzW21M5pY",
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
        "<a href=\"https://colab.research.google.com/github/debasoumya/RS-Python-B/blob/main/Qs_6.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "n=1000\n",
        "prime=[True] * (n+1)\n",
        "def sieveOfEratosthenes(n):\n",
        "  prime[1]=False\n",
        "  a=2\n",
        "  b=0\n",
        "  while a*a<=n:\n",
        "    b+=1\n",
        "    if (prime[a] == True) :\n",
        "      for i in range(a*2,n+1,a):\n",
        "        prime[i] = False\n",
        "    a+=1\n",
        "def findDiff(arr,c):\n",
        "  min=n+2\n",
        "  max=-1\n",
        "  for i in range(c):\n",
        "    if(prime[arr[i]]== True):\n",
        "      if(arr[i]>max):\n",
        "        max=arr[i]\n",
        "      if(arr[i]<min):\n",
        "        min=arr[i]\n",
        "      return -1 if (max==-1) else (max-min)\n",
        "if __name__ == \"__main__\" :\n",
        "  sieveOfEratosthenes(n)\n",
        "  c=5\n",
        "  arr=[1,2,4,5,9]\n",
        "  d=findDiff(arr,c)\n",
        "  if(d==-1):\n",
        "    print(\"no prime numbers\")\n",
        "  else:\n",
        "    print(\"difference is\",d )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IVrpGPBexnCd",
        "outputId": "eb92abd1-5d3a-4fe1-a635-c958c2f5a5c5"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "difference is 0\n"
          ]
        }
      ]
    }
  ]
}