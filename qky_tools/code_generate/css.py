def generate_tailwind(save_dir):
    with open(save_dir, 'w+', encoding='utf-8') as f:

        # rem 比例部分
        for i in range(200):
            for prefix, style in [
                ('ml', 'margin-left'),
                ('mr', 'margin-right'),
                ('mt', 'margin-top'),
                ('mb', 'margin-bottom'),
                ('m', 'margin'),

                ('pl', 'padding-left'),
                ('pr', 'padding-right'),
                ('pt', 'padding-top'),
                ('pb', 'padding-bottom'),
                ('p', 'padding'),

                ('w', 'width'),
                ('h', 'height'),

                ('min-w', 'min-width'),
                ('min-h', 'min-height'),

                ('max-w', 'max-width'),
                ('max-h', 'max-height'),

                ('line-height', 'line-height'),

                ('r', 'border-radius'),


            ]:
                _style = "." + f'{prefix}-{i}' + "{\n" + f'\t{style}: {i / 10}rem;' + "\n}\n\n"
                f.write(_style)

        # 宽度高度
        for wh, width_height in [('w', 'width'), ('h', 'height')]:

            # 百分比部分
            for width_sep_count in range(1, 51):
                for i in range(1, width_sep_count):
                    class_name = f".{wh}-{i}\/{width_sep_count}"
                    _style = f"{width_height}: {100 * i / width_sep_count}%;"
                    f.write(class_name + '\n{\n\t' + _style +'\n};\n')

        # 固定样式部分
        f.write("""
            .flex{display: flex};
            .flex-col{flex-direction: column;};
            .inline-block{display: inline-block};
            .items-center{align-items: center;};
            .text-center{text-align: center;};
            .inline-block{display: inline-block};
            .h-full{height: 100%};
            .w-full{width: 100%};
            
            .bl{border-left: solid 1px #e8e8e8};
            .br{border-right: solid 1px #e8e8e8}; 
            
            .bg-white{background: white};        
            .flex-end{justify-content: flex-end;};   
            
            .overflow-auto{overflow:auto};
            
            .grid-2 {
              display: grid;
              grid-template-columns: repeat(2, 49%);
            };
            .grid-3 {
              display: grid;
              grid-template-columns: repeat(3, 33%);
            };
        """)

    ...


generate_tailwind("d:/mytail.css")
