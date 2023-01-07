{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNBS3dG6ZIcmr8R2NoGhutr",
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
        "<a href=\"https://colab.research.google.com/github/Wata-Naoki/leetcode/blob/main/27(easy).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LsZ4g3Iuh8Be",
        "outputId": "272f6eca-25f5-4556-8d79-d646baa820b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 2 2 3\n",
            "3\n",
            "(2, [2, 2])\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def main(nums, val):\n",
        "  k=0\n",
        "  for i in nums:\n",
        "    if i != val:\n",
        "      nums[k]=i\n",
        "      k += 1\n",
        "  return k\n",
        "\n",
        "\n",
        "nums=[int(x) for x in input().split()]\n",
        "val=int(input())\n",
        "print(main(nums, val))"
      ]
    }
  ]
}