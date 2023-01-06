{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPcTu97dzhcWKKbXPdGcN3q",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/leetcode/blob/main/26(easy).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xZ06dIzBfzxC",
        "outputId": "24dfb871-9fd8-4b05-fdb9-4a3af30c34f4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 \n",
            "{1, 2, 3}\n"
          ]
        }
      ],
      "source": [
        "nums=[int(x) for x in input().split()]\n",
        "\n",
        "print(set(nums))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nums=[int(x) for x in input().split()]\n",
        "n=0\n",
        "for i in range(1, len(nums)):\n",
        "  if nums[n]<nums[i]:\n",
        "      n+=1\n",
        "      nums[n]=nums[i]\n",
        "  \n",
        "print(n+1)\n"
      ],
      "metadata": {
        "id": "ECgH0UmOjIHa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}