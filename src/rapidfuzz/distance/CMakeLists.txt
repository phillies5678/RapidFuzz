function(create_cython_target _name)
    if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/${_name}.cxx)
        set(${_name} ${CMAKE_CURRENT_LIST_DIR}/${_name}.cxx PARENT_SCOPE)
    else()
        find_package(Cython REQUIRED)
        # should use target_include_directories once this is supported by scikit-build
        include_directories(${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
        add_cython_target(${_name} CXX)
        set(${_name} ${_name} PARENT_SCOPE)
    endif()
endfunction(create_cython_target)

create_cython_target(_initialize_cpp)
add_library(_initialize_cpp MODULE ${_initialize_cpp})
target_compile_features(_initialize_cpp PUBLIC cxx_std_14)
target_include_directories(_initialize_cpp PRIVATE ${RF_CAPI_PATH} ${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
target_link_libraries(_initialize_cpp PRIVATE rapidfuzz::rapidfuzz jaro_winkler::jaro_winkler)
python_extension_module(_initialize_cpp)
install(TARGETS _initialize_cpp LIBRARY DESTINATION src/rapidfuzz/distance)

create_cython_target(Hamming_cpp)
add_library(Hamming_cpp MODULE ${Hamming_cpp})
target_compile_features(Hamming_cpp PUBLIC cxx_std_14)
target_include_directories(Hamming_cpp PRIVATE ${RF_CAPI_PATH} ${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
target_link_libraries(Hamming_cpp PRIVATE rapidfuzz::rapidfuzz jaro_winkler::jaro_winkler)
python_extension_module(Hamming_cpp)
install(TARGETS Hamming_cpp LIBRARY DESTINATION src/rapidfuzz/distance)

create_cython_target(Levenshtein_cpp)
add_library(Levenshtein_cpp MODULE ${Levenshtein_cpp})
target_compile_features(Levenshtein_cpp PUBLIC cxx_std_14)
target_include_directories(Levenshtein_cpp PRIVATE ${RF_CAPI_PATH} ${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
target_link_libraries(Levenshtein_cpp PRIVATE rapidfuzz::rapidfuzz jaro_winkler::jaro_winkler)
python_extension_module(Levenshtein_cpp)
install(TARGETS Levenshtein_cpp LIBRARY DESTINATION src/rapidfuzz/distance)

create_cython_target(Indel_cpp)
add_library(Indel_cpp MODULE ${Indel_cpp})
target_compile_features(Indel_cpp PUBLIC cxx_std_14)
target_include_directories(Indel_cpp PRIVATE ${RF_CAPI_PATH} ${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
target_link_libraries(Indel_cpp PRIVATE rapidfuzz::rapidfuzz jaro_winkler::jaro_winkler)
python_extension_module(Indel_cpp)
install(TARGETS Indel_cpp LIBRARY DESTINATION src/rapidfuzz/distance)

create_cython_target(LCSseq_cpp)
add_library(LCSseq_cpp MODULE ${LCSseq_cpp})
target_compile_features(LCSseq_cpp PUBLIC cxx_std_14)
target_include_directories(LCSseq_cpp PRIVATE ${RF_CAPI_PATH} ${RF_BASE_DIR}/rapidfuzz ${RF_BASE_DIR}/rapidfuzz/distance)
target_link_libraries(LCSseq_cpp PRIVATE rapidfuzz::rapidfuzz jaro_winkler::jaro_winkler)
python_extension_module(LCSseq_cpp)
install(TARGETS LCSseq_cpp LIBRARY DESTINATION src/rapidfuzz/distance)