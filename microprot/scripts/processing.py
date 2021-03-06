#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tomasz Kosciolek"
__version__ = "1.01b"
__last_update__ = "12/19/2016"


import click
import sys
from skbio import io, Sequence


def extract_sequences(infile, seqidx=0):
    """ Extract sequence(s) from a multi-sequence FASTA file

    Parameters
    ----------
    infile : str
        file path to input multi-sequence FASTA file
    seqidx : int (optional)
        n-th sequence of the input file to extract
        (default: 0 for all sequences)

    Returns
    -------
    list of skbio Sequence
    """
    seqs = []
    iseq = 0  # current sequence index
    for seq in io.read(infile, format='fasta'):
        iseq += 1
        if 0 < seqidx != iseq:
            continue
        seqs.append(seq)
    return seqs


@click.command()
@click.option('--infile', '-i', required=True,
              type=click.Path(resolve_path=True, readable=True, exists=True,
                              file_okay=True),
              help='Input protein sequence file in FASTA format')
@click.option('--seqidx', '-s', default=0,
              help='Extract n-th sequence (default: all sequences)')
def _main(infile, outfile, seqidx):
    """ Parsing arguments for processing
    """
    extract_sequences(infile, seqidx)


if __name__ == "__main__":
    main()
