import cairo

from io import BytesIO
from IPython.core import display
import numpy as np
import math

def display_cairo_surface(surface):
    """Displayhook function for Surfaces Images, rendered as PNG."""
    b = BytesIO()

    surface.write_to_png(b)
    b.seek(0)
    data = b.read()

    ip_img = display.Image(data=data, format='png', embed=True)
    return ip_img #._repr_png_()


def display_cairo_context(ctx):
    """Displayhook function for cairo Context Images, target is rendered as PNG."""
    surface = ctx.get_target()
    return display_cairo_surface(surface)
  
def ellipse():
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
  context = cairo.Context(surface)
  #context.scale(100, 100) 
  context.set_source_rgba(0,0,0,1)
  s = np.random.rand() / 3
  #context.transform(mtx)
  context.scale(100,100)
  displacement_x = 0.5 + (np.random.rand() - 0.5 ) / 2
  displacement_y = 0.5 + (np.random.rand() - 0.5 ) / 2
  context.translate(displacement_x, displacement_y)
  context.rotate(np.random.rand() * math.pi)
  s = 0.1 + np.random.rand() / 6
  context.scale(0.6,0.6 + np.random.rand()/4) 
  #context.rotate(np.random.rand() * math.pi)
  context.arc(0,0, s, 0, 2*math.pi)
  context.fill()
  return surface

def triangle():
    # Triangle
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
  context = cairo.Context(surface)
  context.scale(25, 25)
  context.set_source_rgba(0,0,0,1)
  s = np.random.rand() / 2
  displacement_x = (np.random.rand() + 1)
  displacement_y = (np.random.rand() + 1)
  context.translate(displacement_x, displacement_y)
  context.rotate(np.random.rand() * math.pi)
  context.scale((np.random.rand() + 0.5),(np.random.rand() + 0.5))
  context.move_to(0, 0)
  context.line_to(0, 1)
  context.line_to(1, 0)
  context.line_to(0, 0)
  #context.stroke()
  context.fill()
  return surface

def parallelogram():
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 100, 100)
  context = cairo.Context(surface)
  context.set_source_rgb(0,0,0)
  #context.rectangle(0, 0, 30, 30)
  #context.fill()
  context.scale(25, 25) 
  displacement_x = (np.random.rand() + 1)
  displacement_y = (np.random.rand() + 1)
  
  context.translate(displacement_x, displacement_y)

  shear_x = (np.random.rand() - 0.5) / 2
  shear_y = (np.random.rand() - 0.5) / 2
  
  mtx = cairo.Matrix(1,shear_x,
                shear_y, 1,
                0, 0 )
  context.transform(mtx)
  context.rotate(np.random.rand() * math.pi)

  context.rectangle(0, 0, 1, 1)

  context.fill()
  return surface

def surface_data(s):
  return np.array(s.get_data()).reshape(100,100,4)[:,:,-1].reshape(100*100)


  
def foo(): 
  return 1
