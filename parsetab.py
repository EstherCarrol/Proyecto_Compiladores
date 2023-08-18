
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BINARIO DOMINO EOF HEXADECIMAL ID MAYA NUMERO OCTAL ROMANOconversion : NUMERO sistema_conversionsistema_conversion : ID'
    
_lr_action_items = {'NUMERO':([0,],[2,]),'$end':([1,3,4,],[0,-1,-2,]),'ID':([2,],[4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'conversion':([0,],[1,]),'sistema_conversion':([2,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> conversion","S'",1,None,None,None),
  ('conversion -> NUMERO sistema_conversion','conversion',2,'p_conversion','Proyecto_compiladores.py',521),
  ('sistema_conversion -> ID','sistema_conversion',1,'p_sistema_conversion','Proyecto_compiladores.py',526),
]