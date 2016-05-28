#!/usr/bin/env python

import sys, getopt


def usage():
    print '%s:Usage [-o|-p|-r] [--help]' % (sys.argv[0]);


def genvalues_xml(out_file_name, px_max, scale):
    value_xml = '<?xml version="1.0" encoding="utf-8"?>'
    value_xml += '<resources>\n'
    for i in range(0, px_max + 1):
        value_xml += '\t<dimen name="p%d">%0.1fpx</dimen>\n' % (i, i * scale)
    value_xml += '</resources>'
    f = file(out_file_name, "w+")
    f.write(value_xml)
    f.close()


if __name__ == "__main__":

    out_xml_file = ""
    px_max = 1920
    scale = 1.0

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:p:r:", ["help", "outFile", "pxMAX", "scale"])
        for op, value in opts:
            if op == "-o":
                out_xml_file = value
            elif op == "-p":
                px_max = int(value)
            elif op == "-r":
                scale = float(value)
            elif op == "-h":
                usage()
                sys.exit()
            else:
                usage()
                sys.exit()

        if out_xml_file.isspace():
            print 'error input'
            usage()
            sys.exit()

        print 'gen dimens.xml:out_file=%s,max_px=%d,scale=%f' % (out_xml_file, px_max, scale)
        genvalues_xml(out_xml_file, px_max, scale)
        print 'gen xml success!'

    except getopt.GetoptError:
        print ("getopt error!")
        usage()
        sys.exit(1)
