# struct: Binary Data Structures
# The struct module includes functions for converting between strings of bytes and native Python 
# data types such as numbers and strings.

import array
import binascii
import ctypes
import struct


# ----------------------------------
# Functions Versus Struct Class
# A set of module-level functions is available for working with structured values, as well as the 
# Struct class. Format specifiers are converted from their string format to a compiled representation, 
# similar to the way regular expressions are handled. The conversion takes some resources, so it 
# is typically more efficient to do it once when creating a Struct instance and call methods on 
# the instance instead of using the module-level functions. All of the following examples use the 
# Struct class

# ----------------------------------
# Packing and Unpacking
# Structs support packing data into strings, and unpacking data from strings using format specifiers 
# made up of characters representing the type of the data and optional count and endianness indicators. 
# Refer to the standard library documentation for a complete list of the supported format specifiers.

values = (1, 'ab'.encode('ascii'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('Original values:', values)
print('Format string :', s.format)
print('Uses :', s.size, 'bytes')
print('Packed Value :', binascii.hexlify(packed_data))

# binascii.hexlify() converts the packed value to a sequence of hex bytes for printing
# Use unpack() to extract data from its packed representation.

s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
print('Unpacked Values:', unpacked_data)


# ----------------------------------
# Endianness

endianness = [
    ('@', 'native, native'),
    ('=', 'native, standard'),
    ('<', 'little-endian'),
    ('>', 'big-endian'),
    ('!', 'network'),
]

for code, name in endianness:
    s = struct.Struct(code + ' I 2s f')
    packed_data = s.pack(*values)
    print()
    print('Format string :', "'%s'"%s.format, 'for', name)
    print('Uses :', s.size, 'bytes')
    print('Packed Value :', binascii.hexlify(packed_data))
    print('Unpacked Value :', s.unpack(packed_data))


# ----------------------------------
# Buffers
# Working with binary packed data is typically reserved for performance-sensitive situations 
# or passing data into and out of extension modules. These cases can be optimized by avoiding
# the overhead of allocating a new buffer for each packed structure. The pack_into() and unpack_from() 
# methods support writing to pre-allocated buffers directly.

print('ctypes string buffer')
b = ctypes.create_string_buffer(s.size)
print("Before  :", binascii.hexlify(b.raw))
s.pack_into(b, 0, *values)
print('After   :', binascii.hexlify(b.raw))
print('Unpacked:', s.unpack_from(b, 0))
print('array')
a = array.array('b', b'\1' * s.size)
print("Before  :", binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('After   :', binascii.hexlify(a))
print('Unpacked:', s.unpack_from(a, 0))