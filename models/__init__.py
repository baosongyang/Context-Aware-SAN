# coding=utf-8
# Copyright 2018 The THUMT Authors

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import thumt.models.seq2seq
import thumt.models.rnnsearch
import thumt.models.transformer
import thumt.models.transformer_new
import thumt.models.transformer_adp
import thumt.models.transformer_local
import thumt.models.transformer_conv
import thumt.models.transformer_pos
import thumt.models.transformer_context_di

def get_model(name):
    name = name.lower()

    if name == "rnnsearch":
        return thumt.models.rnnsearch.RNNsearch
    elif name == "seq2seq":
        return thumt.models.seq2seq.Seq2Seq
    elif name == "transformer":
        return thumt.models.transformer.Transformer
    elif name == "transformer_new":
        return thumt.models.transformer_new.Transformer
    elif name == "transformer_local":
        return thumt.models.transformer_local.Transformer
    elif name == "transformer_pos":
        return thumt.models.transformer_pos.Transformer
    elif name == "transformer_block":
        return thumt.models.transformer_block.Transformer
    elif name == "transformer_di":
        return thumt.models.transformer_context_di.Transformer
    elif name == "transformer_conv":
        return thumt.models.transformer_conv.Transformer
    elif name == "transformer_adp":
        return thumt.models.transformer_adp.Transformer
    else:
        raise LookupError("Unknown model %s" % name)
