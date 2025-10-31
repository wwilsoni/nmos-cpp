from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os

class NmosCppConan(ConanFile):
    name = "nmos-cpp"
    version = "4.12.0"
    package_type = "library"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = [
        "boost/1.83.0",
        "cpprestsdk/2.10.18",
        "websocketpp/0.8.2",
        "openssl/3.1.3",
        "json-schema-validator/2.1.0",
        "spdlog/1.12.0"
    ]

    def layout(self):
        cmake_layout(self, src_folder="src")
        print(">>> Source folder:", self.source_folder)

    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="src")
        cmake.build()
        print(">>> Source folder:", self.source_folder)

    def package(self):
        cmake = CMake(self)
        cmake.install()
        print(">>> Source folder:", self.source_folder)

    def package_info(self):
        self.cpp_info.libs = ["nmos-cpp"]
        print(">>> Source folder:", self.source_folder)