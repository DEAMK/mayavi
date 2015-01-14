# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.object import Object


class Pen(Object):
    """
    Pen - provides a pen that draws the outlines of shapes drawn
    
    Superclass: Object
    
    The Pen defines the outline of shapes that are drawn by
    Context2D. The color is stored as four unsigned chars (RGBA),
    where the opacity defaults to 255, but can be modified separately to
    the other components. Ideally we would use a lightweight color class
    to store and pass around colors.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkPen, obj, update, **traits)
    
    def _get_color(self):
        return self._vtk_obj.GetColor()
    def _set_color(self, arg):
        old_val = self._get_color()
        self._wrap_call(self._vtk_obj.SetColor,
                        arg)
        self.trait_property_changed('color', old_val, arg)
    color = traits.Property(_get_color, _set_color, help=\
        """
        Get the color of the brush - expects an unsigned char of length
        3.
        """
    )

    opacity = traits.Int(255, enter_set=True, auto_set=False, help=\
        """
        Set the opacity with an unsigned char, ranging from 0
        (transparent) to 255 (opaque).
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    width = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the width of the pen.
        """
    )
    def _width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetWidth,
                        self.width)

    line_type = traits.Int(1, enter_set=True, auto_set=False, help=\
        """
        Set the type of line that the pen should draw. The default is
        solid (1).
        """
    )
    def _line_type_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetLineType,
                        self.line_type)

    def get_color_f(self, *args):
        """
        V.get_color_f([float, float, float])
        C++: void GetColorF(double color[3])
        Get the color of the brush - expects a double of length 3 to copy
        into.
        """
        ret = self._wrap_call(self._vtk_obj.GetColorF, *args)
        return ret

    def set_color_f(self, *args):
        """
        V.set_color_f([float, float, float])
        C++: void SetColorF(double color[3])
        V.set_color_f(float, float, float)
        C++: void SetColorF(double r, double g, double b)
        V.set_color_f(float, float, float, float)
        C++: void SetColorF(double r, double g, double b, double a)
        Set the color of the brush with three component doubles (RGB),
        ranging from 0.0 to 1.0.
        """
        ret = self._wrap_call(self._vtk_obj.SetColorF, *args)
        return ret

    def deep_copy(self, *args):
        """
        V.deep_copy(Pen)
        C++: void DeepCopy(Pen *pen)
        Make a deep copy of the supplied pen.
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.DeepCopy, *my_args)
        return ret

    def set_opacity_f(self, *args):
        """
        V.set_opacity_f(float)
        C++: void SetOpacityF(double a)
        Set the opacity with a double, ranging from 0.0 (transparent) to
        1.0 (opaque).
        """
        ret = self._wrap_call(self._vtk_obj.SetOpacityF, *args)
        return ret

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('width', 'GetWidth'), ('line_type',
    'GetLineType'), ('global_warning_display', 'GetGlobalWarningDisplay'),
    ('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'line_type', 'opacity', 'width'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(Pen, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit Pen properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['line_type', 'opacity', 'width']),
            title='Edit Pen properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit Pen properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
