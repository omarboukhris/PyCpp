
from observers import Observer, HppGenerator, TemplGenerator, CppGenerator, GatewayGenerator, PyGwGenerator
from streams import StringStream, FileStream

from typing import List

class FileNameProcessor:
	"""
	Processes filenames in a list appropriately depending on
	the file to generate
	Supported extensions: cpp, h, py, ctype, impl

	Can be used in Factories or passed as a parameter to CMakeGenerator
	"""

	def __init__(self, files: List[str] = None, ext: List[str] = None):
		""" Constructor

		:param files: list of files
		:param ext: list of extensions
		"""
		self.files = files if files else []
		self.ext = ext if ext else []
		self._cleanup_ext()

	def _cleanup_ext(self) -> None:
		""" Cleans up extension from file names
		"""
		out = []
		for proc in self.files:
			cln_file_name = "".join(proc.split(".")[:-1])
			out.append(cln_file_name)
		self.files = out

	#
	# Helper methods
	#

	def get_files(self) -> List[str]:
		"""	Accessor to list of cleaned up files
		"""
		return self.files

	def make_cpp(self) -> str:
		""" called in CMakeGenerator, helper method

		:return: C++ generated file name
		"""
		if "cpp" in self.ext:
			return self._make_ext("cpp")
		return ""

	def make_h(self) -> str:
		""" called in CMakeGenerator, helper method

		:return: header (h/hpp) generated file name
		"""
		if "h" in self.ext:
			return self._make_ext("h")
		return ""

	def make_impl(self) -> str:
		""" called in CMakeGenerator, helper method

		:return: impl generated file name
		"""
		if "impl" in self.ext:
			return self._make_ext("impl")
		return ""

	def make_py(self) -> str:
		if "py" in self.ext:
			return self._make_ext("py")
		return ""

	def make_gw(self) -> str:
		if "ctype" in self.ext:
			return self._make_prefix_ext("pyGw_", "cpp")
		return ""

	def _make_ext(self, ext: str) -> str:
		""" Decorate file names with extension

		:param ext: extension decorating file names
		:return: decorated file names
		"""
		return self._make_prefix_ext("", ext)

	def _make_prefix_ext(self, pref: str, ext: str) -> str:
		""" Decorate file names with prefix and extension
		filenames/have/this/structure/w/o/extension

		:param pref: prefix
		:param ext: extension
		:return: decorated file names list
		"""
		files = []
		if pref:
			# add prefix to the last element in path (filename)
			for f in self.files:
				fsplit = f.split("/")
				fname = pref + fsplit[-1]
				full_fname = "/".join(fsplit[:-1] + [fname])
				files.append(full_fname[1:])
		else:
			files = [f[1:] for f in self.files]
		ss = "\t" + "\n\t".join(["{}.{}".format(f, ext) for f in files])
		return ss

class HelperFactory:

	def __init__ (self, pname: str, ppath: str):
		self.pname = pname
		self.ppath = ppath

	@classmethod
	def single_fn_fabric(cls, fname: str, ext: str, pref: str = "") -> str:
		""" Single File Name Factory

		:param fname: file name
		:param ext: file extension
		:param pref: file prefix
		:return: constructed file name
		"""
		fname = "".join(fname.split(".")[:-1])  # remove extension
		if pref:
			# add prefix to the last element in path (filename)class Observer:

			fsplit = fname.split("/")
			new_fname = pref + fsplit[-1]
			fname = "/".join(fsplit[:-1] + [new_fname])
		ss = "{}.{}".format(fname, ext)
		return ss

	@classmethod
	def file_stream_fabric(cls, fname: str, out_ext: List[str] = None) -> List[FileStream]:
		""" File Stream Factory

		:param fname: file name
		:param out_ext: output extension
		:return: list of initialized file streams
		"""
		out_ext = out_ext if out_ext else []
		out = []
		for ext in out_ext:
			pref = ""
			if ext in ["ctype"]:
				pref = "pyGw_"
				ext = "cpp"
			if ext in ["cpp", "h", "hpp", "py", "impl", "ctype"]:
				out.append(FileStream(
					fname=cls.single_fn_fabric(
						fname=fname,
						ext=ext,
						pref=pref
					)
				))

		# add __init__.py file
		if "py" in out_ext:
			initfilepath = "/".join(fname.split("/")[:-1]) + "/__init__.py"
			out.append(FileStream(fname=initfilepath))
		return out

	@classmethod
	def string_stream_fabric(cls, out_ext: List[str] = None) -> List[StringStream]:
		""" String Stream Factory

		:param out_ext: output extension
		:return: list of initialized String streams
		"""
		out_ext = out_ext if out_ext else []
		out = []
		for ext in out_ext:
			if ext in ["cpp", "h", "hpp", "py", "ctype", "impl"]:
				out.append(StringStream())
		return out

	def generator_fabric(
		self,
		filename: str,
		out_ext: List[str] = None,
		streams: List[FileStream] = None
	) -> List[Observer]:
		""" Generator Factory
		Associates streams to generators

		:param filename: currently processed file name
		:param out_ext: output extensions
		:param streams: File or String streams to write into
		:return: list of generators to use as observers parameters in PyCppEngine
		"""
		out = []
		for ext, stream in zip(out_ext, streams):
			if ext in ["cpp"]:
				cpp_generator = CppGenerator(stream)
				cpp_generator.set_header_filename(filename)
				out.append(cpp_generator)
			elif ext in ["h", "hpp"]:
				out.append(HppGenerator(stream))
			elif ext in ["py"]:
				pygw = PyGwGenerator(stream)
				pygw.set_lib_path(self.pname, self.ppath)
				out.append(pygw)
			elif ext in ["ctype"]:
				gw_generator = GatewayGenerator(stream)
				gw_generator.set_header_filename(filename)
				out.append(gw_generator)
			elif ext in ["impl"]:
				out.append(TemplGenerator(stream))
		return out
