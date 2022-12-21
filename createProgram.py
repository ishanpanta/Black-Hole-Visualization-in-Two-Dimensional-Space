import OpenGL.GL as gl

# This function initializes and links all the compiled shader 
# to a program object which is later used to render our objects
def createProgram(vertex, fragment):
    program = gl.glCreateProgram()
    gl.glAttachShader(program, vertex)
    gl.glAttachShader(program, fragment)

    gl.glLinkProgram(program)
    if not gl.glGetProgramiv(program, gl.GL_LINK_STATUS):
        print(gl.glGetProgramInfoLog(program))
        raise RuntimeError("Error Linking program")

    gl.glDetachShader(program, vertex)
    gl.glDetachShader(program, fragment)

    return program
