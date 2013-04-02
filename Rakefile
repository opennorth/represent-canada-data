desc 'Checks that directories contain a LICENSE.txt file'
task :check do
  def check(path = '.')
    entries = Dir.new(path).entries.reject do |entry|
      entry[0] == '.' || entry == 'examples'
    end

    paths = entries.map do |entry|
      File.join(path, entry)
    end

    directories = paths.select do |path|
      File.directory?(path)
    end

    unless paths.size == directories.size
      puts "No LICENSE.txt found in #{path}" unless entries.include?('LICENSE.txt')
    end

    directories.each do |directory|
      check(directory)
    end
  end

  check
end
