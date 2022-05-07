# coding: utf-8

from maya import cmds
from kmt_tool.kmt_export import kmt_export_gui

def main_menu():
    cmds.menu( label='kmt_tool', parent='MayaWindow', tearOff=True )
    
    cmds.menuItem( label='motion', tearOff=True, subMenu=True )
    cmds.menuItem( label='export',c = 'kmt_export_gui.main()' )
    cmds.setParent( '..', menu=True )