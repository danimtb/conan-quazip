import os
from conans import ConanFile, CMake, tools

class quazipConan(ConanFile):
    name = "quazip"
    version = "0.7.3"
    description = "A C++/Qt ZIP library"
    homepage = "http://quazip.sourceforge.net/"
    url = "https://sourceforge.net/projects/quazip"
    license = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False]
        }
    default_options = "shared=True"
    requires = "zlib/1.2.8@conan/stable", "Qt/5.8.0@osechet/testing"

    def source(self):
        tools.get("%s/files/%s/%s/%s-%s.zip" % (self.url, self.name, self.version, self.name,
                                                self.version))
        os.rename("%s-%s" % (self.name, self.version), "sources")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="sources")
        cmake.build()

    def package(self):
        with tools.chdir("sources"):
            self.copy(pattern="LICENSE", dst="licenses", src="sources", ignore_case=True,
                      keep_path=False)

            self.copy(pattern="*.h", dst="include", src="sources")

        self.copy(pattern="*.dll", dst="bin", src="lib", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
