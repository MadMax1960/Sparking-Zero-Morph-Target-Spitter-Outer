import bpy

def reorder_shape_keys(target_order):
    obj = bpy.context.active_object
    
    if obj is None or not obj.data.shape_keys:
        print(f"Error: No active object selected or the selected object has no shape keys.")
        return
    
    shape_key_block = obj.data.shape_keys
    shape_keys = shape_key_block.key_blocks
    
    # Extract existing shape keys excluding Basis
    existing_shape_keys = [key.name for key in shape_keys if key.name != 'Basis']
    
    # Verify that every shape key in the target_order exists in the mesh
    for key in target_order:
        key = key.strip()
        if key and key not in existing_shape_keys:
            print(f"Error: Shape key '{key}' not found in the active object.")
            return
    
    # Create a new list of shape keys by reordering according to the target_order
    reordered_shape_keys = ['Basis']  # Basis should always be at index 0
    reordered_shape_keys.extend([key.strip() for key in target_order if key.strip()])  # Remove empty lines
    
    # Reorder the shape keys by using new indices
    for key_name in reordered_shape_keys[::-1]:
        shape_key = shape_keys.get(key_name)
        if shape_key:
            obj.active_shape_key_index = shape_key_block.key_blocks.keys().index(key_name)
            bpy.ops.object.shape_key_move(type='TOP')
    
    print("Shape keys reordered successfully.")

# Example usage
example_list = """
LMT_00_Normal1
LMT_01_Clench1
LMT_01_Shout1
LMT_02_Smile2
LMT_06_Clench3
LMT_06_Shout3
LMT_07_Displeasure1
LMT_07_Displeasure2
LMT_09_Smile1
MT_D_EAR1
MT_D_Eye1
MT_D_Mouth1
MT_D_Nose1
MT_Default1_R
MT_E_Anger1
MT_E_Anger2
MT_E_Anger3
MT_E_Calm1
MT_E_CloseBothEyes1
MT_E_CloseBothEyes2
MT_E_CloseRightEye1
MT_E_Surprise1
MT_E_Surprise3
MT_Sweat1
""".splitlines()

# Run the function on the selected object
reorder_shape_keys(example_list)