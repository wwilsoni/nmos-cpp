from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
import os
print(">>> source_folder:", self.source_folder)
print(">>> contents:", os.listdir(self.source_folder))

class NmosCppConan(ConanFile):
    name = "nmos-cpp"
    version = "4.12.0"
    package_type = "library"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "CMakeList.txt", "src/*", "cmake/*", "include/*"
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
        cmake_layout(self)


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()


    def package(self):
        cmake = CMake(self)
        cmake.install()


    def package_info(self):
        print(">>> [package_info] package_folder:", self.package_folder)
        self.cpp_info.libs = ["nmos-cpp"]