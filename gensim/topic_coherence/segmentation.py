#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Radim Rehurek <radimrehurek@seznam.cz>
# Licensed under the GNU LGPL v2.1 - http://www.gnu.org/licenses/lgpl.html

"""
This module contains functions to perform segmentation on a list of topics.
"""

import logging
import numpy as np

logger = logging.getLogger(__name__)

def s_one_pre(topics):
    """
    This function performs s_one_pre segmentation on a list of topics.
    s_one_pre segmentation is defined as: s_one_pre = {(W', W*) | W' = {w_i};
                                                                  W* = {w_j}; w_i, w_j belongs to W; i > j}
    Example:

        >>> topics = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> s_one_pre(topics)
        [[(2, 1), (3, 1), (3, 2)], [(5, 4), (6, 4), (6, 5)]]

    Args:
    ----
    topics : list of topics obtained from an algorithm such as LDA. Is a list such as [array([ 9, 10, 11]), array([ 9, 10,  7]), ...]

    Returns:
    -------
    s_one_pre : list of list of (W', W*) tuples for all unique topic ids
    """
    s_one_pre = []

    for top_words in topics:
        s_one_pre_t = []
        for w_prime in top_words[1:]:
            w_prime_index = np.where(top_words == w_prime)[0] # To get index of w_star in top_words
            for w_star in top_words[:w_prime_index]:
                s_one_pre_t.append((w_prime, w_star))
        s_one_pre.append(s_one_pre_t)

    return s_one_pre

def s_one_set(topics):
    """
    This function performs s_one_set segmentation on a list of topics.
    s_one_set segmentation is defined as: s_one_set = {(W', W*) | W' = {w_i}; w_i belongs to W;
                                                                  W* = W}
    Example:
        >>> topics = [np.array([9, 10, 7])
        >>> s_one_set(topics)
        [[(9, array([ 9, 10,  7])),
          (10, array([ 9, 10,  7])),
          (7, array([ 9, 10,  7]))]]

    Args:
    ----
    topics : list of topics obtained from an algorithm such as LDA. Is a list such as [array([ 9, 10, 11]), array([ 9, 10,  7]), ...]

    Returns:
    -------
    s_one_set : list of list of (W', W*) tuples for all unique topic ids.
    """
    s_one_set = []

    for top_words in topics:
        s_one_set_t = []
        for w_prime in top_words:
            s_one_set_t.append((w_prime, top_words))
        s_one_set.append(s_one_set_t)

    return s_one_set
