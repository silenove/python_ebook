# -*- coding: utf-8 -*-
from enthought.traits.api import HasTraits, Str, Int
from enthought.traits.ui.api import *

class SimpleEmployee(HasTraits):
    first_name = Str
    last_name = Str
    department = Str

    employee_number = Str
    salary = Int
    bonus = Int

view1 = View(
    VGroup(
        VGrid(
            Item(name = 'employee_number', label=u'编号'),
            Item(name = 'department', label=u"部门", tooltip=u"在哪个部门干活"),
            Item(name = 'last_name', label=u"姓"),
            Item(name = 'first_name', label=u"名"),
            label = u'个人信息',
            show_border = True,
            scrollable = True
        ),
        VGroup(
            Item(name = 'salary', label=u"工资"),
            Item(name = 'bonus', label=u"奖金"),
            label = u'收入',
            show_border = True,
        )   
    ), 
    resizable = True,
    width = 400,
    height = 150
)

sam = SimpleEmployee()
sam.configure_traits(view=view1)