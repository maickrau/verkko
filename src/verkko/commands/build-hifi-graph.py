import sys
import inspect

import verkkoConfig as vC
import verkkoHelper as vH    #  For 'ruleOutput' and 'ruleInputs'

#  See comments in verkko.py, please.
def synopsis():
  #     -90-columns-------------------------------------------------------------------------------
  s=f'''use HiFi reads to build an initial assembly graph'''
  return inspect.cleandoc(s)

def details():
  #     -90-columns-------------------------------------------------------------------------------
  s=f'''build-hifi-graph ...

        Vestibulum ut gravida metus, nec laoreet massa. Integer vitae
        ullamcorper felis, pellentesque aliquam nisi. Interdum et malesuada
        fames ac ante ipsum primis in faucibus. Donec ac dui sed mi vehicula
        aliquam non non metus. Nulla mattis augue sapien, eget aliquet urna
        tincidunt vitae. Phasellus dignissim est sollicitudin nunc dignissim
        accumsan vel id est. Phasellus vel arcu placerat, convallis neque eu,
        vestibulum mi. Morbi blandit et enim eget hendrerit. Nulla
        facilisi. Quisque ornare elementum quam, nec bibendum elit molestie
        id. Proin in enim eu dolor accumsan dapibus non in odio. Nulla ut
        mauris ut felis ullamcorper accumsan sed non turpis. Cras viverra sit
        amet velit in consequat. Cras efficitur arcu nisi, id ornare odio
        viverra ut. In hac habitasse platea dictumst.'''
  return inspect.cleandoc(s)


#
#  Workflow description and parameters.
#

def inputs(rules, wildcards, checkpoints):
  return {}

def outputs(rules):
  return { 'hifi-finished': '1-reads/hifi-finished' }

def logs(rules):
  return {}

def params(rules):
  return {}

def threads(rules):
  return 4

def resources(rules):
  return {}

#
#  Sub-command execution.
#

def run(cConfig):
  pass
