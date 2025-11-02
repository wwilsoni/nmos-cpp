from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class NmosCppConan(ConanFile):
    name = "nmos-cpp"
    version = "4.12.0"
    package_type = "library"

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    exports_sources = "CMakeLists.txt", "Development/*", "cmake/*", "LICENSE", "NOTICE", "README.md"
    requires = [
        "boost/1.83.0",
        "cpprestsdk/2.10.18",
        "websocketpp/0.8.2",
        "openssl/3.1.3",
        "json-schema-validator/2.1.0",
        "jwt-cpp/0.7.1",
    ]

    def layout(self):
        cmake_layout(self, src_folder="Development")

    def build(self):
        cmake = CMake(self)
        cmake.configure(variables={
            "BUILD_TESTING": "OFF",
            "NMOS_CPP_BUILD_TESTS": "OFF"
        })
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # Export a proper CMake package
        self.cpp_info.set_property("cmake_file_name", "nmos-cpp")
        self.cpp_info.set_property("cmake_target_name", "nmos-cpp::nmos-cpp")

        # Libraries to link (adjust if your CMake actually produces a different name)
        self.cpp_info.libs = ["nmos-cpp"]

        # Propagate dependencies downstream
        self.cpp_info.requires = [
            "boost::boost",
            "cpprestsdk::cpprest",
            "websocketpp::websocketpp",
            "openssl::openssl",
            "nlohmann_json_schema_validator::nlohmann_json_schema_validator",
            "jwt-cpp::jwt-cpp"
        ]

