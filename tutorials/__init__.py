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
  
def ellipse(context):
  context.save()
  #context.scale(100, 100) 
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
  context.restore()

def triangle(context):
    # Triangle
  context.save()  
  context.scale(25, 25)
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
  context.restore()

def parallelogram(context):
  context.save()
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
  context.restore()


def surface_data(s):
  return np.array(s.get_data()).reshape(100,100,4)[:,:,-1].reshape(100*100)

    # Text
    #surface = cairo.SVGSurface("example.svg", 300, 100)
    #cr = cairo.Context(surface)
    #cr.set_source_rgb(0.1, 0.1, 0.1)
    #context.scale(100, 100) 
        
    #cr.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
    #    cairo.FONT_WEIGHT_NORMAL)
    #cr.set_font_size(13)
    
    #cr.move_to(20, 30)
    #cr.show_text("Most relationships seem so transitory")
    #display_cairo_surface(surface)
    
    
def raster(dims, directives):
  surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, dims[0], dims[1])
  context = cairo.Context(surface) 
  for d in directives:
    d(context)
  return surface  

def raster_png(dims, directives):
  s = raster(dims, directives)
  return display_cairo_surface(s)

def raster_np(dims, directives):
  s = raster(dims, directives)
  return np.array(s.get_data()).reshape(dims[0],dims[1],4)
  
def foo(): 
  return 1
