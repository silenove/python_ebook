# -*- coding: utf-8 -*-
# filename: traits_property.py
from enthought.traits.api import HasTraits, Float, Property, cached_property

class Rectangle(HasTraits):
    width = Float(1.0) 
    height = Float(2.0)

    #area是一个属性，当width,height的值变化时，它对应的_get_area函数将被调用
    area = Property(depends_on=['width', 'height']) 

    # 通过cached_property decorator缓存_get_area函数的输出
    @cached_property 
    def _get_area(self):
        """
        area的get函数，注意此函数名和对应的Proerty名的关系
        """
        print 'recalculating'
        return self.width * self.height
